from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
from ..models import db, User, League
from ..forms.league_form import LeagueForm

league_routes = Blueprint('leagues', __name__)


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


# CREATE A LEAGUE
@league_routes.route('<int:id>/new', methods=["POST"])
def create_league(id):

    form = LeagueForm()
    user = User.query.get(id)
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        data = form.data

        new_league = League(
            name = data['name'],
            commissioner_id = user.id,
            draft_type = data['draft_type'],
            scoring_system = data['scoring_system'],
            max_teams = data['max_teams']
        )

        db.session.add(new_league)
        db.session.commit()

        return new_league.to_dict(), 200

    return {'errors': form.errors}, 400

#EDIT A LEAGUE
@league_routes.route('/<int:id>', methods=["PUT"])
def edit_league(id):

    data = request.json()
    league = League.query.get(id)

    if not league:
        return {"Error": "There is no league to edit"}, 400

    if 'name' in data:
        league.name = data['name']

    if 'draft_type' in data:
        league.draft_type = data['draft_type']

    if 'scoring_system' in data:
        league.scoring_system = data['scoring_system']

    if 'max_teams' in data:
        league.max_teams = data['max_teams']

    db.session.commit()

    return league.to_dict(), 200

#DELETE A LEAGUE
@league_routes.route('/<int:id>/delete', methods=["DELETE"])
def delete_league(id):

    league = League.query.get(id)

    if not league:
        return {"Error": "This league does not exist"}, 400

    db.session.delete(league)
    db.session.commit()

    return {"Message": "League was successfully deleted"}
