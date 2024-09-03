from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
from ..models import db, User, League, Team
from ..forms.league_form import LeagueForm
from .aws_utils import upload_file_to_s3, get_unique_filename, remove_file_from_s3

league_routes = Blueprint('leagues', __name__)

# Allowed file extensions for image uploads
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# GET ALL LEAGUES
@league_routes.route('/')
def get_all_leagues():

    league = League.query.all()

    leagues_list = [l.to_dict() for l in league]

    return leagues_list


# GET A SINGLE LEAGUE
@league_routes.route('/<int:id>')
def get_single_league(id):

    league = League.query.get(id)

    return league.to_dict()


#GET ALL TEAMS IN A LEAGUE
@league_routes.route('/<int:id>/teams')
def get_all_teams_in_league(id):

    teams = Team.query.filter_by(league_id=id).all()

    teams_list = [team.to_dict() for team in teams]

    return teams_list


# CREATE A LEAGUE
@league_routes.route('/new', methods=["POST"])
def create_league():
    form = LeagueForm()
    form["csrf_token"].data = request.cookies.get("csrf_token")

    if form.validate_on_submit():
        data = form.data
        print('Form Data >>>>>>>', data)

        image = request.files.get('image')
        image_url = None

        if not allowed_file(image.filename):
                print(f"Error: File type not permitted for filename {image.filename}")
                return ({"errors": "File type not permitted"}), 400

        if image and image.filename:
            image.filename = get_unique_filename(image.filename)
            upload_result = upload_file_to_s3(image)

            if 'url' not in upload_result:
                print(f"Error: File upload failed with result {upload_result}")
                return {"errors": upload_result.get('errors', 'File upload failed')}, 400

            image_url = upload_result['url']
            print(f"Image uploaded successfully: {image_url}")

        # Create the new league object
        new_league = League(
            name=data['name'],
            commissioner_id=current_user.id,
            draft_type=data['draft_type'],
            scoring_system=data['scoring_system'],
            max_teams=data['max_teams'],
            image_url=image_url  # Set to None if no image uploaded
        )

        print('New league >>>>>>>>>>>>>>>>>>>>>', new_league)
        db.session.add(new_league)
        db.session.commit()

        return new_league.to_dict(), 200

    return {'errors': form.errors}, 400


#EDIT A LEAGUE
@league_routes.route('/<int:id>', methods=["PUT"])
def edit_league(id):
    form = LeagueForm()
    form["csrf_token"].data = request.cookies.get("csrf_token")

    league = League.query.get(id)
    if not league:
        return {"Error": "There is no league to edit"}, 400

    if form.validate_on_submit():
        data = form.data
        print('Form Data >>>>>>>', data)

        image = request.files.get('image')
        image_url = league.image_url  # Retain the old image URL if no new image is uploaded

        if not allowed_file(image.filename):
                print(f"Error: File type not permitted for filename {image.filename}")
                return ({"errors": "File type not permitted"}), 400

        if image and image.filename:
            image.filename = get_unique_filename(image.filename)
            upload_result = upload_file_to_s3(image)

            if 'url' not in upload_result:
                print(f"Error: File upload failed with result {upload_result}")
                return {"errors": upload_result.get('errors', 'File upload failed')}, 400

            image_url = upload_result['url']
            print(f"Image uploaded successfully: {image_url}")

        # Update the league object
        league.name = data['name']
        league.draft_type = data['draft_type']
        league.scoring_system = data['scoring_system']
        league.max_teams = data['max_teams']
        league.image_url = image_url  # Update image URL with new one

        print('Updated league >>>>>>>>>>>>>>>>>>>>>', league)
        db.session.commit()

        return league.to_dict(), 200

    return {'errors': form.errors}, 400


#DELETE A LEAGUE
@league_routes.route('/<int:id>', methods=["DELETE"])
def delete_league(id):

    league = League.query.get(id)

    if not league:
        return {"Error": "This league does not exist"}, 400

    db.session.delete(league)
    db.session.commit()

    return {"Message": "League was successfully deleted"}, 200
