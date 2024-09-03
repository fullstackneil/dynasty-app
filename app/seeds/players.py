from app.models import db, Player, environment, SCHEMA
from sqlalchemy.sql import text


def seed_players():

    players = [
        Player(first_name='Christian', last_name='McCaffrey', position='RB', team='San Francisco 49ers', average_draft_position=1.0, points_last_season=350.5, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330754/01._Christian_McCaffrey_ihqgxr.png'),
        Player(first_name='CeeDee', last_name='Lamb', position='WR', team='Dallas Cowboys', average_draft_position=2.0, points_last_season=290.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330754/02._CeeDee_Lamb_tfiya5.png'),
        Player(first_name='Tyreek', last_name='Hill', position='WR', team='Miami Dolphins', average_draft_position=3.0, points_last_season=300.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330755/03._Tyreek_Hill_hmt12q.png'),
        Player(first_name='Breece', last_name='Hall', position='RB', team='New York Jets', average_draft_position=4.0, points_last_season=275.2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330755/04._Breece_Hall_foc5jc.png'),
        Player(first_name='Bijan', last_name='Robinson', position='RB', team='Atlanta Falcons', average_draft_position=5.0, points_last_season=250.1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330756/05._Bijan_Robinson_okvj8m.png'),
        Player(first_name="Ja'Marr", last_name='Chase', position='WR', team='Cincinnati Bengals', average_draft_position=6.0, points_last_season=230.3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330757/06._Ja_Marr_Chase_ykz9ya.png'),
        Player(first_name='Amon-Ra', last_name='St. Brown', position='WR', team='Detroit Lions', average_draft_position=7.0, points_last_season=310.7, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330757/07._Amon-Ra_St._Brown_o5njtl.png'),
        Player(first_name='Justin', last_name='Jefferson', position='WR', team='Minnesota Vikings', average_draft_position=8.0, points_last_season=220.5, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330759/08._Justin_Jefferson_denjcy.png'),
        Player(first_name='A.J.', last_name='Brown', position='WR', team='Philadelphia Eagles', average_draft_position=9.0, points_last_season=230.8, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330758/09._A.J._Brown_vmeiz5.png'),
        Player(first_name='Garrett', last_name='Wilson', position='WR', team='New York Jets', average_draft_position=10.0, points_last_season=205.9, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330761/10._Garrett_Wilson_immfbc.png'),
        Player(first_name='Jonathan', last_name='Taylor', position='RB', team='Indianapolis Colts', average_draft_position=11.0, points_last_season=240.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330760/11._Jonathan_Taylor_aitysz.png'),
        Player(first_name='Jahmyr', last_name='Gibbs', position='RB', team='Detroit Lions', average_draft_position=12.0, points_last_season=210.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330760/12._Jahmyr_Gibbs_uejpg8.png'),
        Player(first_name='Saquon', last_name='Barkley', position='RB', team='Philadelphia Eagles', average_draft_position=13.0, points_last_season=190.7, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330762/13._Saquon_Barkley_g4gdbc.png'),
        Player(first_name='Puka', last_name='Nacua', position='WR', team='Los Angeles Rams', average_draft_position=14.0, points_last_season=185.5, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330764/14._Puka_Nacua_nxqf3g.png'),
        Player(first_name='Marvin', last_name='Harrison Jr.', position='WR', team='Arizona Cardinals', average_draft_position=15.0, points_last_season=200.3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330767/15._Marvin_Harrison_Jr._a9rq2y.png'),
        Player(first_name='Drake', last_name='London', position='WR', team='Atlanta Falcons', average_draft_position=16.0, points_last_season=175.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330762/16._Drake_London_xcdz77.png'),
        Player(first_name='Derrick', last_name='Henry', position='RB', team='Baltimore Ravens', average_draft_position=17.0, points_last_season=175.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330764/17._Derrick_Henry_ebodb1.png'),
        Player(first_name='Travis', last_name='Etienne Jr.', position='RB', team='Jacksonville Jaguars', average_draft_position=18.0, points_last_season=180.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330772/18._Travis_Etienne_Jr._dqg02c.png'),
        Player(first_name='Davante', last_name='Adams', position='WR', team='Las Vegas Raiders', average_draft_position=19.0, points_last_season=160.3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330766/19._Davante_Adams_tgkjze.png'),
        Player(first_name='Chris', last_name='Olave', position='WR', team='New Orleans Saints', average_draft_position=20.0, points_last_season=245.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330766/20._Chris_Olave_z6gtql.png'),
        Player(first_name='Mike', last_name='Evans', position='WR', team='Tampa Bay Buccaneers', average_draft_position=21.0, points_last_season=140.2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330770/21._Mike_Evans_gsvq39.png'),
        Player(first_name='Kyren', last_name='Williams', position='RB', team='Los Angeles Rams', average_draft_position=22.0, points_last_season=185.7, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330769/22._Kyren_Williams_jkouht.png'),
        Player(first_name='Deebo', last_name='Samuel Sr.', position='WR', team='San Francisco 49ers', average_draft_position=23.0, points_last_season=170.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330769/23._Deebo_Samuel_Jr._zfhu6o.png'),
        Player(first_name='Nico', last_name='Collins', position='WR', team='Houston Texans', average_draft_position=24.0, points_last_season=165.9, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330773/24._Nico_Collins_jkqroa.png'),
        Player(first_name='Josh', last_name='Allen', position='QB', team='Buffalo Bills', average_draft_position=25.0, points_last_season=155.2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330774/25._Josh_Allen_mpwvhd.png'),
        Player(first_name='Isiah', last_name='Pacheco', position='RB', team='Kansas City Chiefs', average_draft_position=26.0, points_last_season=275.5, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330775/26._Isiah_Pacheco_cpvmw9.png'),
        Player(first_name='Brandon', last_name='Aiyuk', position='WR', team='San Francisco 49ers', average_draft_position=27.0, points_last_season=235.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330777/27._Brandon_Aiyuk_n4yzb9.png'),
        Player(first_name="De'Von", last_name='Achane', position='RB', team='Miami Dolphins', average_draft_position=28.0, points_last_season=190.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330777/28._De_Von_Achane_ancgj5.png'),
        Player(first_name='Jaylen', last_name='Waddle', position='WR', team='Miami Dolphins', average_draft_position=29.0, points_last_season=145.3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330779/29._Jaylen_Waddle_pb68k5.png'),
        Player(first_name='Cooper', last_name='Kupp', position='WR', team='Los Angeles Rams', average_draft_position=30.0, points_last_season=175.8, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330780/30._Cooper_Kupp_kazpyf.png'),
        Player(first_name='Jalen', last_name='Hurts', position='QB', team='Philadelphia Eagles', average_draft_position=31.0, points_last_season=160.5, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330781/31._Jalen_Hurts_izec46.png'),
        Player(first_name='Sam', last_name='LaPorta', position='TE', team='Detroit Lions', average_draft_position=32.0, points_last_season=155.9, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330782/32._Sam_LaPorta_s48bgi.png'),
        Player(first_name='DK', last_name='Metcalf', position='WR', team='Seattle Seahawks', average_draft_position=33.0, points_last_season=130.2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330784/33._DK_Metcalf_zefhud.png'),
        Player(first_name='Travis', last_name='Kelce', position='TE', team='Kansas City Chiefs', average_draft_position=34.0, points_last_season=170.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330784/34._Travis_Kelce_ktqgck.png'),
        Player(first_name='Josh', last_name='Jacobs', position='RB', team='Green Bay Packers', average_draft_position=35.0, points_last_season=145.7, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330785/35._Josh_Jacobs_ek2slt.png'),
        Player(first_name='Patrick', last_name='Mahomes', position='QB', team='Kansas City Chiefs', average_draft_position=36.0, points_last_season=215.3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330785/36._Patrick_Mahomes_wjmhlo.png'),
        Player(first_name='DJ', last_name='Moore', position='WR', team='Chicago Bears', average_draft_position=37.0, points_last_season=190.7, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330788/37._DJ_Moore_d9o400.png'),
        Player(first_name='Lamar', last_name='Jackson', position='QB', team='Baltimore Ravens', average_draft_position=38.0, points_last_season=205.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330789/38._Lamar_Jackson_oogwhw.png'),
        Player(first_name='Devonta', last_name='Smith', position='WR', team='Philadelphia Eagles', average_draft_position=39.0, points_last_season=150.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330791/39._DeVonta_Smith_e4gtpx.png'),
        Player(first_name='Michael', last_name='Pittman Jr.', position='WR', team='Indianapolis Colts', average_draft_position=40.0, points_last_season=200.1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330791/40._Michael_Pittman_Jr._gryqv6.png'),
        Player(first_name='Malik', last_name='Nabers', position='WR', team='New York Giants', average_draft_position=41.0, points_last_season=180.2, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330795/41._Malik_Nabers_tb8fgv.png'),
        Player(first_name='Kenneth', last_name='Walker III', position='RB', team='Seattle Seahawks', average_draft_position=42.0, points_last_season=140.5, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330793/42._Kenneth_Walker_III_unqt38.png'),
        Player(first_name='Amari', last_name='Cooper', position='WR', team='Cleveland Browns', average_draft_position=43.0, points_last_season=165.7, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330799/43._Amari_Cooper_za69iq.png'),
        Player(first_name='James', last_name='Cook', position='RB', team='Buffalo Bills', average_draft_position=44.0, points_last_season=200.9, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330794/44._James_Cook_zyhgxm.png'),
        Player(first_name='Rachaad', last_name='White', position='RB', team='Tampa Bay Buccaneers', average_draft_position=45.0, points_last_season=130.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330796/45._Rachaad_White_d92tyn.png'),
        Player(first_name='Joe', last_name='Mixon', position='RB', team='Houston Texans', average_draft_position=46.0, points_last_season=150.1, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330801/46._Joe_Mixon_xpuzgm.png'),
        Player(first_name='Tee', last_name='Higgins', position='WR', team='Cincinnati Bengals', average_draft_position=47.0, points_last_season=120.3, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330798/47._Tee_Higgins_hgpqkr.png'),
        Player(first_name='Mark', last_name='Andrews', position='TE', team='Baltimore Ravens', average_draft_position=48.0, points_last_season=145.8, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330798/48._Mark_Andrews_ky4frv.png'),
        Player(first_name='Rashee', last_name='Rice', position='WR', team='Kansas City Chiefs', average_draft_position=49.0, points_last_season=135.9, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330802/49._Rashee_Rice_xuxy1v.png'),
        Player(first_name='Alvin', last_name='Kamara', position='RB', team='New Orleans Saints', average_draft_position=50.0, points_last_season=160.4, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330804/50._Alvin_Kamara_cfq7dc.png'),
        Player(first_name='Trey', last_name='McBride', position='TE', team='Arizona Cardinals', average_draft_position=51.0, points_last_season=150.6, image_url='https://res.cloudinary.com/dw0k7r34f/image/upload/v1725330804/51._Trey_McBride_iw8j66.png'),
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
