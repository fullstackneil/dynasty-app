from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
import random
from ..models import db, User, League, Team
from ..forms import TeamForm
from .aws_utils import upload_file_to_s3, get_unique_filename, remove_file_from_s3


team_routes = Blueprint('teams', __name__)

# Allowed file extensions for image uploads
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# GET A SINGLE TEAM
@team_routes.route('/<int:id>')
def get_single_team(id):

    team = Team.query.get(id)

    return team.to_dict()


# GET ALL TEAMS OWNED BY A SPECIFIC USER
@team_routes.route('/user/<int:id>')
def get_all_teams_from_user(id):

    teams = Team.query.filter_by(user_id=id).all()

    teams_list = [team.to_dict() for team in teams]

    return teams_list, 200


#CREATE A TEAM
@team_routes.route('/<int:id>/create', methods=["POST"])
def create_team(id):
    form = TeamForm()

    # Set CSRF token
    form["csrf_token"].data = request.cookies["csrf_token"]

    if not form.validate_on_submit():
        return {'Error': form.errors}, 400

    # Retrieve the league to get the max number of teams
    league = League.query.get(id)
    if not league:
        return {'Error': 'League not found'}, 404

    # Image processing
    image = request.files.get('image')
    image_url = None

    if image and image.filename:
        image.filename = get_unique_filename(image.filename)
        upload_result = upload_file_to_s3(image)

        if 'url' not in upload_result:
            return {"errors": upload_result.get('errors', 'File upload failed')}, 400

        image_url = upload_result['url']

    # Draft position logic
    max_teams = league.max_teams
    existing_positions = {team.draft_position for team in Team.query.filter_by(league_id=id).all()}

    draft_position = random.randint(1, max_teams)
    while draft_position in existing_positions:
        draft_position = random.randint(1, max_teams)

    # Create new team
    new_team = Team(
        name=form.data['name'],
        league_id=id,  # Use the league_id from the URL
        user_id=current_user.id,  # Use the current user's ID
        draft_position=draft_position,  # Random number
        image_url=image_url
    )

    db.session.add(new_team)
    db.session.commit()

    return new_team.to_dict(), 200



# EDIT A TEAM
@team_routes.route('/<int:id>', methods=["PUT"])
def update_team(id):
    team = Team.query.get(id)

    if not team:
        return {'Error': 'This team does not exist.'}, 404

    # Create and validate the form
    form = TeamForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if not form.validate_on_submit():
        return {'Error': form.errors}, 400

    # Image processing
    image = request.files.get('image')
    if image and image.filename and allowed_file(image.filename):
        if team.image_url:
            # Remove the old image from S3
            remove_file_from_s3(team.image_url)

        # Process and upload new image
        image.filename = get_unique_filename(image.filename)
        upload_result = upload_file_to_s3(image)

        if 'url' not in upload_result:
            return {"Error": upload_result.get('errors', 'File upload failed')}, 400

        # Update team with new image URL
        team.image_url = upload_result['url']

    # Update team details from form data
    if 'name' in form.data:
        team.name = form.data['name']

    if 'league_id' in form.data:
        team.league_id = form.data['league_id']

    if 'user_id' in form.data:
        team.user_id = form.data['user_id']

    if 'draft_position' in form.data:
        team.draft_position = form.data['draft_position']

    db.session.commit()

    return team.to_dict(), 200


#DELETE A TEAM
@team_routes.route('/<int:team_id>', methods=["DELETE"])
def delete_team(team_id):

    team = Team.query.get(team_id)

    if not team:
        return {'Error': 'This team does not exist.'}

    db.session.delete(team)
    db.session.commit()

    return {'Message': 'Team successfully deleted'}, 200
