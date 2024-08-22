from app.models import db, Player, environment, SCHEMA
from sqlalchemy.sql import text


def seed_players():

    players = [
        Player(first_name='Patrick', last_name='Mahomes', position='QB', team='Kansas City Chiefs', average_draft_position=1.0, points_last_season=350.5, image_url='https://example.com/images/patrick-mahomes.jpg'),
        Player(first_name='Davante', last_name='Adams', position='WR', team='Las Vegas Raiders', average_draft_position=2.0, points_last_season=290.4, image_url='https://example.com/images/davante-adams.jpg'),
        Player(first_name='Derrick', last_name='Henry', position='RB', team='Tennessee Titans', average_draft_position=3.0, points_last_season=300.6, image_url='https://example.com/images/derrick-henry.jpg'),
        Player(first_name='Tyreek', last_name='Hill', position='WR', team='Miami Dolphins', average_draft_position=4.0, points_last_season=275.2, image_url='https://example.com/images/tyreek-hill.jpg'),
        Player(first_name='Austin', last_name='Ekeler', position='RB', team='Los Angeles Chargers', average_draft_position=5.0, points_last_season=250.1, image_url='https://example.com/images/austin-ekeler.jpg'),
        Player(first_name='Travis', last_name='Kelce', position='TE', team='Kansas City Chiefs', average_draft_position=6.0, points_last_season=230.3, image_url='https://example.com/images/travis-kelce.jpg'),
        Player(first_name='Josh', last_name='Allen', position='QB', team='Buffalo Bills', average_draft_position=7.0, points_last_season=310.7, image_url='https://example.com/images/josh-allen.jpg'),
        Player(first_name='DeAndre', last_name='Hopkins', position='WR', team='Tennessee Titans', average_draft_position=8.0, points_last_season=220.5, image_url='https://example.com/images/deandre-hopkins.jpg'),
        Player(first_name='Najee', last_name='Harris', position='RB', team='Pittsburgh Steelers', average_draft_position=9.0, points_last_season=230.8, image_url='https://example.com/images/najee-harris.jpg'),
        Player(first_name='George', last_name='Kittle', position='TE', team='San Francisco 49ers', average_draft_position=10.0, points_last_season=205.9, image_url='https://example.com/images/george-kittle.jpg'),
        Player(first_name='Jalen', last_name='Hurts', position='QB', team='Philadelphia Eagles', average_draft_position=11.0, points_last_season=240.6, image_url='https://example.com/images/jalen-hurts.jpg'),
        Player(first_name='Stefon', last_name='Diggs', position='WR', team='Buffalo Bills', average_draft_position=12.0, points_last_season=210.4, image_url='https://example.com/images/stefon-diggs.jpg'),
        Player(first_name='Ezekiel', last_name='Elliott', position='RB', team='Dallas Cowboys', average_draft_position=13.0, points_last_season=190.7, image_url='https://example.com/images/ezekiel-elliott.jpg'),
        Player(first_name='Mark', last_name='Andrews', position='TE', team='Baltimore Ravens', average_draft_position=14.0, points_last_season=185.5, image_url='https://example.com/images/mark-andrews.jpg'),
        Player(first_name='Aaron', last_name='Jones', position='RB', team='Green Bay Packers', average_draft_position=15.0, points_last_season=200.3, image_url='https://example.com/images/aaron-jones.jpg'),
        Player(first_name='Keenan', last_name='Allen', position='WR', team='Los Angeles Chargers', average_draft_position=16.0, points_last_season=175.6, image_url='https://example.com/images/keenan-allen.jpg'),
        Player(first_name='Saquon', last_name='Barkley', position='RB', team='New York Giants', average_draft_position=17.0, points_last_season=180.4, image_url='https://example.com/images/saquon-barkley.jpg'),
        Player(first_name='Terry', last_name='McLaurin', position='WR', team='Washington Commanders', average_draft_position=18.0, points_last_season=160.3, image_url='https://example.com/images/terry-mclaurin.jpg'),
        Player(first_name='Justin', last_name='Jefferson', position='WR', team='Minnesota Vikings', average_draft_position=19.0, points_last_season=245.6, image_url='https://example.com/images/justin-jefferson.jpg'),
        Player(first_name='Clyde', last_name='Edwards-Helaire', position='RB', team='Kansas City Chiefs', average_draft_position=20.0, points_last_season=140.2, image_url='https://example.com/images/clyde-edwards-helaire.jpg'),
        Player(first_name='Mike', last_name='Evans', position='WR', team='Tampa Bay Buccaneers', average_draft_position=21.0, points_last_season=185.7, image_url='https://example.com/images/mike-evans.jpg'),
        Player(first_name='Josh', last_name='Jacobs', position='RB', team='Las Vegas Raiders', average_draft_position=22.0, points_last_season=170.4, image_url='https://example.com/images/josh-jacobs.jpg'),
        Player(first_name='Darren', last_name='Waller', position='TE', team='Las Vegas Raiders', average_draft_position=23.0, points_last_season=165.9, image_url='https://example.com/images/darren-waller.jpg'),
        Player(first_name='James', last_name='Robinson', position='RB', team='Jacksonville Jaguars', average_draft_position=24.0, points_last_season=155.2, image_url='https://example.com/images/james-robinson.jpg'),
        Player(first_name='Cooper', last_name='Kupp', position='WR', team='Los Angeles Rams', average_draft_position=25.0, points_last_season=275.5, image_url='https://example.com/images/cooper-kupp.jpg'),
        Player(first_name='Lamar', last_name='Jackson', position='QB', team='Baltimore Ravens', average_draft_position=26.0, points_last_season=235.4, image_url='https://example.com/images/lamar-jackson.jpg'),
        Player(first_name='Chris', last_name='Godwin', position='WR', team='Tampa Bay Buccaneers', average_draft_position=27.0, points_last_season=190.6, image_url='https://example.com/images/chris-godwin.jpg'),
        Player(first_name='David', last_name='Montgomery', position='RB', team='Chicago Bears', average_draft_position=28.0, points_last_season=145.3, image_url='https://example.com/images/david-montgomery.jpg'),
        Player(first_name='Amari', last_name='Cooper', position='WR', team='Cleveland Browns', average_draft_position=29.0, points_last_season=175.8, image_url='https://example.com/images/amari-cooper.jpg'),
        Player(first_name='Robby', last_name='Anderson', position='WR', team='Carolina Panthers', average_draft_position=30.0, points_last_season=160.5, image_url='https://example.com/images/robby-anderson.jpg'),
        Player(first_name='Miles', last_name='Sanders', position='RB', team='Philadelphia Eagles', average_draft_position=31.0, points_last_season=155.9, image_url='https://example.com/images/miles-sanders.jpg'),
        Player(first_name='Harrison', last_name='Butker', position='K', team='Kansas City Chiefs', average_draft_position=32.0, points_last_season=130.2, image_url='https://example.com/images/harrison-butker.jpg'),
        Player(first_name='Tyler', last_name='Lockett', position='WR', team='Seattle Seahawks', average_draft_position=33.0, points_last_season=170.4, image_url='https://example.com/images/tyler-lockett.jpg'),
        Player(first_name='Robert', last_name='Woods', position='WR', team='Tennessee Titans', average_draft_position=34.0, points_last_season=145.7, image_url='https://example.com/images/robert-woods.jpg'),
        Player(first_name='Kirk', last_name='Cousins', position='QB', team='Minnesota Vikings', average_draft_position=35.0, points_last_season=215.3, image_url='https://example.com/images/kirk-cousins.jpg'),
        Player(first_name='Zeke', last_name='Elliott', position='RB', team='Dallas Cowboys', average_draft_position=36.0, points_last_season=190.7, image_url='https://example.com/images/zeke-elliott.jpg'),
        Player(first_name='Deebo', last_name='Samuel', position='WR', team='San Francisco 49ers', average_draft_position=37.0, points_last_season=205.6, image_url='https://example.com/images/deebo-samuel.jpg'),
        Player(first_name='Juju', last_name='Smith-Schuster', position='WR', team='Kansas City Chiefs', average_draft_position=38.0, points_last_season=150.4, image_url='https://example.com/images/juju-smith-schuster.jpg'),
        Player(first_name='Tua', last_name='Tagovailoa', position='QB', team='Miami Dolphins', average_draft_position=39.0, points_last_season=200.1, image_url='https://example.com/images/tua-tagovailoa.jpg'),
        Player(first_name='Diontae', last_name='Johnson', position='WR', team='Pittsburgh Steelers', average_draft_position=40.0, points_last_season=180.2, image_url='https://example.com/images/diontae-johnson.jpg'),
        Player(first_name='Melvin', last_name='Gordon', position='RB', team='Denver Broncos', average_draft_position=41.0, points_last_season=140.5, image_url='https://example.com/images/melvin-gordon.jpg'),
        Player(first_name='Chase', last_name='Claypool', position='WR', team='Pittsburgh Steelers', average_draft_position=42.0, points_last_season=165.7, image_url='https://example.com/images/chase-claypool.jpg'),
        Player(first_name='Darren', last_name='Waller', position='TE', team='Las Vegas Raiders', average_draft_position=43.0, points_last_season=200.9, image_url='https://example.com/images/darren-waller.jpg'),
        Player(first_name='Hunter', last_name='Henry', position='TE', team='New England Patriots', average_draft_position=44.0, points_last_season=130.4, image_url='https://example.com/images/hunter-henry.jpg'),
        Player(first_name='Chris', last_name='Carson', position='RB', team='Seattle Seahawks', average_draft_position=45.0, points_last_season=150.1, image_url='https://example.com/images/chris-carson.jpg'),
        Player(first_name='Zach', last_name='Ertz', position='TE', team='Arizona Cardinals', average_draft_position=46.0, points_last_season=120.3, image_url='https://example.com/images/zach-ertz.jpg'),
        Player(first_name='James', last_name='Conner', position='RB', team='Arizona Cardinals', average_draft_position=47.0, points_last_season=145.8, image_url='https://example.com/images/james-conner.jpg'),
        Player(first_name='Raheem', last_name='Mostert', position='RB', team='Miami Dolphins', average_draft_position=48.0, points_last_season=135.9, image_url='https://example.com/images/raheem-mostert.jpg'),
        Player(first_name='Miles', last_name='Sanders', position='RB', team='Philadelphia Eagles', average_draft_position=49.0, points_last_season=160.4, image_url='https://example.com/images/miles-sanders.jpg'),
        Player(first_name='Kenny', last_name='Golladay', position='WR', team='New York Giants', average_draft_position=50.0, points_last_season=150.6, image_url='https://example.com/images/kenny-golladay.jpg'),
    ]

    db.session.bulk_save_objects(players)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_players():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.players RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM players"))

    db.session.commit()
