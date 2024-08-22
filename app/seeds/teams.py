from app.models import db, Team, environment, SCHEMA
from sqlalchemy.sql import text


def seed_teams():

    teams = [
    # Teams for League 1
    Team(name='Dragonfire Warriors', league_id=1, user_id=1, draft_position=1),
    Team(name='Stormbringer Dragons', league_id=1, user_id=2, draft_position=2),
    Team(name='Thunderstrike Titans', league_id=1, user_id=3, draft_position=3),

    # Teams for League 2
    Team(name='Midnight Knights', league_id=2, user_id=4, draft_position=1),
    Team(name='Mystic Elves', league_id=2, user_id=5, draft_position=2),
    Team(name='Giant’s Fury', league_id=2, user_id=6, draft_position=3),

    # Teams for League 3
    Team(name='Ironclad Sharks', league_id=3, user_id=7, draft_position=1),
    Team(name='Eclipse Eagles', league_id=3, user_id=8, draft_position=2),
    Team(name='Blazing Bears', league_id=3, user_id=9, draft_position=3),

    # Teams for League 4
    Team(name='Ravenous Ravens', league_id=4, user_id=10, draft_position=1),
    Team(name='Hawk’s Talon', league_id=4, user_id=11, draft_position=2),
    Team(name='Lionheart Legends', league_id=4, user_id=12, draft_position=3),

    # Teams for League 5
    Team(name='Phantom Pumas', league_id=5, user_id=13, draft_position=1),
    Team(name='Wolfpack Warriors', league_id=5, user_id=14, draft_position=2),
    Team(name='Firestorm Foxes', league_id=5, user_id=15, draft_position=3),

    ]

    db.session.bulk_save_objects(teams)
    db.session.commit()


    # Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
