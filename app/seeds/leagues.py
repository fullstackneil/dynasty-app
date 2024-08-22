from app.models import db, League, environment, SCHEMA
from sqlalchemy.sql import text

def seed_leagues():

    leagues = [
        League(
            id=1,
            name="Gridiron Glory",
            commissioner_id=1,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=12
        ),
        League(
            id=2,
            name="Fantasy Legends",
            commissioner_id=2,
            draft_type="Auction",
            scoring_system="Standard",
            max_teams=10
        ),
        League(
            id=3,
            name="Champions League",
            commissioner_id=3,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=14
        ),
        League(
            id=4,
            name="The Elite League",
            commissioner_id=4,
            draft_type="Snake",
            scoring_system="Half-PPR",
            max_teams=12
        ),
        League(
            id=5,
            name="Gridiron Titans",
            commissioner_id=5,
            draft_type="Auction",
            scoring_system="Standard",
            max_teams=10
        ),
        League(
            id=6,
            name="Dynasty Warriors",
            commissioner_id=6,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=16
        ),
        League(
            id=7,
            name="The Legends League",
            commissioner_id=7,
            draft_type="Auction",
            scoring_system="Half-PPR",
            max_teams=12
        ),
        League(
            id=8,
            name="Fantasy Football Frenzy",
            commissioner_id=8,
            draft_type="Snake",
            scoring_system="Standard",
            max_teams=14
        ),
        League(
            id=9,
            name="Gridiron Masters",
            commissioner_id=9,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=10
        ),
        League(
            id=10,
            name="Ultimate Football League",
            commissioner_id=10,
            draft_type="Auction",
            scoring_system="Half-PPR",
            max_teams=12
        )
    ]

    db.session.bulk_save_objects(leagues)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_leagues():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.leagues RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM leagues"))

    db.session.commit()
