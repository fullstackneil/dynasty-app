from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
from ..models import db, User, League, Team
from ..forms import TeamForm


team_routes = Blueprint('teams', __name__)


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
def create_team(user_id):

    form = TeamForm()
    data = request.get_json()

    form["csrf_token"].data = request.cookies["csrf_token"]

    if not data:
        return {'Error': 'There was an error processing the form'}

    if form.validate_on_submit():
        new_team = Team(
            name = data['name'],
            league_id = data['league_id'],
            user_id = user_id,
            draft_position = data.get('draft_position')  # This will be the random number
        )

        db.session.add(new_team)
        db.session.commit()

        return {'Message': 'Team was successfully created.'}

    return {'Error': 'Team was not created.'}


# EDIT A TEAM
@team_routes.route('/<int:id>', methods=["PUT"])
def update_team(id):

    data = request.get_json()
    team = Team.query.get(id)

    if not team:
        return {'Error': 'This team does not exist.'}

    if 'name' in data:
        team.name = data['name']

    if 'league_id' in data:
        team.league_id = data['league_id']

    if 'user_id' in data:
        team.user_id = data['user_id']

    if 'draft_position' in data:
        team.draft_position = data['draft_position']

    db.session.commit()

    return team.to_dict(), 200


#DELETE A TEAM
@team_routes.route('/<int:id>', methods=["DELETE"])
def delete_team(id):

    team = Team.query.get(id)

    if not team:
        return {'Error': 'This team does not exist.'}

    db.session.delete(team)
    db.session.commit()

    return {'Message': 'Team was successfully deleted.'}
