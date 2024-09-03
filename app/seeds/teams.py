from app.models import db, Team, environment, SCHEMA
from sqlalchemy.sql import text


def seed_teams():

    teams = [
    # Teams for League 1
    Team(name='Dragonfire Warriors', league_id=1, user_id=1, draft_position=1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344465/01._Dragonfire_Warriors_rrzc8f.jpg' ),
    Team(name='Stormbringer Dragons', league_id=1, user_id=2, draft_position=2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344465/02._Stormbringer_Dragons_icwrxu.jpg'),
    Team(name='Thunderstrike Titans', league_id=1, user_id=3, draft_position=3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344465/03._Thunderstrike_Titans_pvsllz.jpg'),

    # Teams for League 2
    Team(name='Midnight Knights', league_id=2, user_id=4, draft_position=1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344515/04._Midnight_Knights_yumobp.jpg'),
    Team(name='Mystic Elves', league_id=2, user_id=5, draft_position=2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344514/05._Mystic_Elves_cxhsys.jpg'),
    Team(name="Giant’s Fury", league_id=2, user_id=6, draft_position=3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344466/06._Giant_s_Fury_leweds.jpg'),

    # Teams for League 3
    Team(name='Ironclad Sharks', league_id=3, user_id=7, draft_position=1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344516/07._Ironclad_Sharks_v2behe.jpg'),
    Team(name='Eclipse Eagles', league_id=3, user_id=8, draft_position=2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344522/08._Eclipse_Eagles_a2vfi5.jpg'),
    Team(name='Blazing Bears', league_id=3, user_id=9, draft_position=3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344518/09._Blazing_Bears_rk79qd.jpg'),

    # Teams for League 4
    Team(name='Ravenous Ravens', league_id=4, user_id=10, draft_position=1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344517/10._Ravenous_Ravens_undt75.jpg'),
    Team(name="Hawk’s Talon", league_id=4, user_id=11, draft_position=2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344522/11._Hawk_s_Talon_lh2wxg.jpg'),
    Team(name='Lionheart Legends', league_id=4, user_id=12, draft_position=3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344520/12._Lionheart_Legends_vlyl8f.jpg'),

    # Teams for League 5
    Team(name='Phantom Pumas', league_id=5, user_id=13, draft_position=1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344519/13._Phantom_Pumasjpeg_coux8z.jpg'),
    Team(name='Wolfpack Warriors', league_id=5, user_id=14, draft_position=2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344520/14._Wolfpack_Warriors_ezzkgk.jpg'),
    Team(name='Firestorm Foxes', league_id=5, user_id=15, draft_position=3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725344524/15._Firestorm_Foxes_tnh9xk.jpg'),

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
