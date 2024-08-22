from flask.cli import AppGroup
from .users import seed_users, undo_users
from .drafts import seed_drafts, undo_drafts
from .draft_picks import seed_draft_picks, undo_draft_picks
from .leagues import seed_leagues, undo_leagues
from .players import seed_players, undo_players
from .rosters import seed_rosters, undo_rosters
from .teams import seed_teams, undo_teams
from .trades import seed_trades, undo_trades
from .trade_details import seed_trade_details, undo_trade_details

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_trade_details()
        undo_trades()
        undo_players()
        undo_draft_picks()
        undo_drafts()
        undo_rosters()
        undo_teams()
        undo_leagues()
        undo_users()

    seed_users()
    seed_leagues()
    seed_teams()
    seed_rosters()
    seed_drafts()
    seed_draft_picks()
    seed_players()
    seed_trades()
    seed_trade_details()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_trade_details()
    undo_trades()
    undo_players()
    undo_draft_picks()
    undo_drafts()
    undo_rosters()
    undo_teams()
    undo_leagues()
    undo_users()


    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.trade_details RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.trades RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.draft_picks RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.drafts RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.rosters RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.leagues RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM trade_details")
        db.session.execute("DELETE FROM trades")
        db.session.execute("DELETE FROM players")
        db.session.execute("DELETE FROM draft_picks")
        db.session.execute("DELETE FROM drafts")
        db.session.execute("DELETE FROM rosters")
        db.session.execute("DELETE FROM teams")
        db.session.execute("DELETE FROM leagues")
        db.session.execute("DELETE FROM users")

        db.session.commit()
