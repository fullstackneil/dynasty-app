from app.models import db, TradeDetail, environment, SCHEMA
from sqlalchemy.sql import text


def seed_trade_details():

    trade_details = [

        TradeDetail(trade_id=1, player_id=1, from_team_id=1, to_team_id=4),
        TradeDetail(trade_id=1, player_id=2, from_team_id=1, to_team_id=4),
        TradeDetail(trade_id=2, player_id=3, from_team_id=2, to_team_id=5),
        TradeDetail(trade_id=3, player_id=4, from_team_id=3, to_team_id=6),
        TradeDetail(trade_id=4, player_id=5, from_team_id=7, to_team_id=10),

    ]

    db.session.bulk_save_objects(trade_details)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_trade_details():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.trade_details RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM trade_details"))

    db.session.commit()
