from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required
import random
from ..models import db, Player


player_routes = Blueprint('players', __name__)


@player_routes.route('/')
def get_all_players():

    player = Player.query.all();

    players_list = [p.to_dict() for p in player]

    return players_list
