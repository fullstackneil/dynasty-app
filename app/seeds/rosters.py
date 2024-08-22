from app.models import db, Roster, environment, SCHEMA
from sqlalchemy.sql import text


def seed_rosters():

    rosters = [

    Roster(team_id=1, player_id=1, position_slot='QB1'),
    Roster(team_id=1, player_id=2, position_slot='WR1'),
    Roster(team_id=1, player_id=3, position_slot='RB1'),
    Roster(team_id=1, player_id=4, position_slot='WR2'),
    Roster(team_id=1, player_id=5, position_slot='TE1'),
    Roster(team_id=1, player_id=6, position_slot='RB2'),
    Roster(team_id=1, player_id=7, position_slot='QB2'),
    Roster(team_id=2, player_id=8, position_slot='WR1'),
    Roster(team_id=2, player_id=9, position_slot='RB1'),
    Roster(team_id=2, player_id=10, position_slot='TE1'),
    Roster(team_id=2, player_id=11, position_slot='WR2'),
    Roster(team_id=2, player_id=12, position_slot='RB2'),
    Roster(team_id=2, player_id=13, position_slot='QB1'),
    Roster(team_id=2, player_id=14, position_slot='WR3'),
    Roster(team_id=3, player_id=15, position_slot='QB1'),
    Roster(team_id=3, player_id=16, position_slot='RB1'),
    Roster(team_id=3, player_id=17, position_slot='WR1'),
    Roster(team_id=3, player_id=18, position_slot='TE1'),
    Roster(team_id=3, player_id=19, position_slot='WR2'),
    Roster(team_id=3, player_id=20, position_slot='RB2'),
    Roster(team_id=3, player_id=21, position_slot='QB2'),
    Roster(team_id=4, player_id=22, position_slot='WR1'),
    Roster(team_id=4, player_id=23, position_slot='RB1'),
    Roster(team_id=4, player_id=24, position_slot='TE1'),
    Roster(team_id=4, player_id=25, position_slot='WR2'),
    Roster(team_id=4, player_id=26, position_slot='RB2'),
    Roster(team_id=4, player_id=27, position_slot='QB1'),
    Roster(team_id=5, player_id=28, position_slot='WR1'),
    Roster(team_id=5, player_id=29, position_slot='RB1'),
    Roster(team_id=5, player_id=30, position_slot='TE1'),
    Roster(team_id=5, player_id=31, position_slot='WR2'),
    Roster(team_id=5, player_id=32, position_slot='RB2'),
    Roster(team_id=5, player_id=33, position_slot='QB1'),
    Roster(team_id=6, player_id=34, position_slot='WR1'),
    Roster(team_id=6, player_id=35, position_slot='RB1'),
    Roster(team_id=6, player_id=36, position_slot='TE1'),
    Roster(team_id=6, player_id=37, position_slot='WR2'),
    Roster(team_id=6, player_id=38, position_slot='RB2'),
    Roster(team_id=6, player_id=39, position_slot='QB1'),
    Roster(team_id=7, player_id=40, position_slot='WR1'),
    Roster(team_id=7, player_id=41, position_slot='RB1'),
    Roster(team_id=7, player_id=42, position_slot='TE1'),
    Roster(team_id=7, player_id=43, position_slot='WR2'),
    Roster(team_id=7, player_id=44, position_slot='RB2'),
    Roster(team_id=7, player_id=45, position_slot='QB1'),
    Roster(team_id=8, player_id=46, position_slot='WR1'),
    Roster(team_id=8, player_id=47, position_slot='RB1'),
    Roster(team_id=8, player_id=48, position_slot='TE1'),
    Roster(team_id=8, player_id=49, position_slot='WR2'),
    Roster(team_id=8, player_id=50, position_slot='RB2'),

    ]

    db.session.bulk_save_objects(rosters)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_rosters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.rosters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM rosters"))

    db.session.commit()
