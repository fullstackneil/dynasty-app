from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
from ..models import League

league_routes = Blueprint("leagues", __name__)


# # GET ALL LEAGUES
# @league_routes('/')
# def get_all_leagues():

#     leagues = League.query.all()

#     leagues_list = [league.to_dict() for league in leagues]

#     return leagues_list.to_dict()
