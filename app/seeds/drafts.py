from app.models import db, Draft, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_drafts():

    drafts = [
        Draft(
            league_id=1,
            draft_date=datetime(2024, 9, 13, 19, 30),
            draft_type='Snake'
        ),
        Draft(
            league_id=2,
            draft_date=datetime(2024, 9, 30, 14, 0),
            draft_type='Auction'
        ),
        Draft(
            league_id=3,
            draft_date=datetime(2024, 10, 8, 18, 0),
            draft_type='Snake'
        ),
        Draft(
            league_id=4,
            draft_date=datetime(2024, 10, 14, 20, 15),
            draft_type='Keeper'
        ),
        Draft(
            league_id=5,
            draft_date=datetime(2024, 10, 23, 13, 0),
            draft_type='Snake'
        ),
        Draft(
            league_id=6,
            draft_date=datetime(2024, 10, 24, 16, 45),
            draft_type='Dynasty'
        ),
        Draft(
            league_id=7,
            draft_date=datetime(2024, 10, 3, 17, 0),
            draft_type='Auction'
        ),
        Draft(
            league_id=8,
            draft_date=datetime(2024, 9, 19, 19, 0),
            draft_type='Keeper'
        ),
        Draft(
            league_id=9,
            draft_date=datetime(2024, 9, 27, 21, 30),
            draft_type='Dynasty'
        ),
        Draft(
            league_id=10,
            draft_date=datetime(2024, 9, 28, 20, 0),
            draft_type='Snake'
        ),

    ]

    db.session.bulk_save_objects(drafts)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_drafts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.drafts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM drafts"))

    db.session.commit()
