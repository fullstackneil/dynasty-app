from app.models import db, League, environment, SCHEMA
from sqlalchemy.sql import text

def seed_leagues():

    leagues = [
        League(
            name="Gridiron Glory",
            commissioner_id=1,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=12,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136286/01._Gridiron_Glory_wofrqz.jpg'
        ),
        League(
            name="Fantasy Legends",
            commissioner_id=2,
            draft_type="Auction",
            scoring_system="Standard",
            max_teams=10,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136284/02._Fantasy_Legends_bxd5p3.jpg'
        ),
        League(
            name="Champions League",
            commissioner_id=3,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=14,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136283/03._Champions_League_fwvyub.jpg'
        ),
        League(
            name="The Elite League",
            commissioner_id=4,
            draft_type="Snake",
            scoring_system="Half-PPR",
            max_teams=12,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136284/04._Elite_League_dzyexy.jpg'
        ),
        League(
            name="Gridiron Titans",
            commissioner_id=5,
            draft_type="Auction",
            scoring_system="Standard",
            max_teams=10,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136286/05._Gridiron_Titans_fyutx7.jpg'
        ),
        League(
            name="Dynasty Warriors",
            commissioner_id=6,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=16,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136284/06._Dynasty_Warriors_zimnjs.jpg'
        ),
        League(
            name="The Legends League",
            commissioner_id=7,
            draft_type="Auction",
            scoring_system="Half-PPR",
            max_teams=12,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136283/07._The_Legends_League_fgecpq.jpg'
        ),
        League(
            name="Fantasy Football Frenzy",
            commissioner_id=8,
            draft_type="Snake",
            scoring_system="Standard",
            max_teams=14,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136286/08._Fantasy_Football_Frenzy_wefd3c.jpg'
        ),
        League(
            name="Gridiron Masters",
            commissioner_id=9,
            draft_type="Snake",
            scoring_system="PPR",
            max_teams=10,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136283/09._Gridiron_Masters_gr611x.jpg'
        ),
        League(
            name="Ultimate Football League",
            commissioner_id=10,
            draft_type="Auction",
            scoring_system="Half-PPR",
            max_teams=12,
            image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725136282/10._Ultimate_Football_League_ksd0cf.jpg'
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
