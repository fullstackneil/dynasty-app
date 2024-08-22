from app.models import db, Trade, environment, SCHEMA
from sqlalchemy.sql import text


def seed_trades():

    trades = [
        Trade(offering_team_id=1, receiving_team_id=4, status='pending'),
        Trade(offering_team_id=2, receiving_team_id=5, status='accepted'),
        Trade(offering_team_id=3, receiving_team_id=6, status='rejected'),
        Trade(offering_team_id=7, receiving_team_id=10, status='pending'),
        Trade(offering_team_id=8, receiving_team_id=11, status='accepted'),
    ]

    db.session.bulk_save_objects(trades)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_trades():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.trades RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM trades"))

    db.session.commit()
