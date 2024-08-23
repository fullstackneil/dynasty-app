from app.models import db, DraftPick, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_draft_picks():

    draft_picks = [
        DraftPick(
            draft_id=1,
            team_id=1,
            player_id=1,
            round=1,
            created_at=datetime(2024, 7, 15, 10, 30),
            updated_at=datetime(2024, 7, 15, 10, 30)
        ),
        DraftPick(
            draft_id=1,
            team_id=2,
            player_id=2,
            round=1,
            created_at=datetime(2024, 7, 15, 10, 32),
            updated_at=datetime(2024, 7, 15, 10, 32)
        ),
        DraftPick(
            draft_id=1,
            team_id=3,
            player_id=3,
            round=1,
            created_at=datetime(2024, 7, 15, 10, 34),
            updated_at=datetime(2024, 7, 15, 10, 34)
        ),
        DraftPick(
            draft_id=1,
            team_id=4,
            player_id=4,
            round=1,
            created_at=datetime(2024, 7, 15, 10, 36),
            updated_at=datetime(2024, 7, 15, 10, 36)
        ),
        DraftPick(
            draft_id=1,
            team_id=5,
            player_id=5,
            round=1,
            created_at=datetime(2024, 7, 15, 10, 38),
            updated_at=datetime(2024, 7, 15, 10, 38)
        ),
        DraftPick(
            draft_id=1,
            team_id=6,
            player_id=6,
            round=2,
            created_at=datetime(2024, 7, 15, 10, 40),
            updated_at=datetime(2024, 7, 15, 10, 40)
        ),
        DraftPick(
            draft_id=1,
            team_id=7,
            player_id=7,
            round=2,
            created_at=datetime(2024, 7, 15, 10, 42),
            updated_at=datetime(2024, 7, 15, 10, 42)
        ),
        DraftPick(
            draft_id=1,
            team_id=8,
            player_id=8,
            round=2,
            created_at=datetime(2024, 7, 15, 10, 44),
            updated_at=datetime(2024, 7, 15, 10, 44)
        ),
        DraftPick(
            draft_id=1,
            team_id=9,
            player_id=9,
            round=2,
            created_at=datetime(2024, 7, 15, 10, 46),
            updated_at=datetime(2024, 7, 15, 10, 46)
        ),
        DraftPick(
            draft_id=1,
            team_id=10,
            player_id=10,
            round=2,
            created_at=datetime(2024, 7, 15, 10, 48),
            updated_at=datetime(2024, 7, 15, 10, 48)
        )
    ]

    db.session.bulk_save_objects(draft_picks)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_draft_picks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.draft_picks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM draft_picks"))

    db.session.commit()
