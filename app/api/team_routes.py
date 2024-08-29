from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
import random
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
def create_team(id):

    form = TeamForm()
    data = request.get_json()

    form["csrf_token"].data = request.cookies["csrf_token"]

    if not data:
        return {'Error': 'There was an error processing the form'}, 400

    if form.validate_on_submit():

        # Retrieve the league to get the max number of teams
        league = League.query.get(id)

        if not league:
            return {'Error': 'League not found'}, 404

        # Get the max number of teams allowed in the league
        max_teams = league.max_teams
        existing_positions = {team.draft_position for team in Team.query.filter_by(league_id=id).all()}

        draft_position = random.randint(1, max_teams)
        while draft_position in existing_positions:
            draft_position = random.randint(1, max_teams)


        new_team = Team(
            name = data['name'],
            league_id = id, # Use the league_id from the URL
            user_id = current_user.id,  # Use the current user's ID (current_user generated from flask_login)
            draft_position=draft_position  # Random number or user input
        )

        db.session.add(new_team)
        db.session.commit()

        return new_team.to_dict(), 200

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
@team_routes.route('/<int:team_id>', methods=["DELETE"])
def delete_team(team_id):

    team = Team.query.get(team_id)

    if not team:
        return {'Error': 'This team does not exist.'}

    db.session.delete(team)
    db.session.commit()

    return {'Message': 'Team successfully deleted'}, 200
