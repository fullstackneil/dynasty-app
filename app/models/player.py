from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Player(db.Model):
    __tablename__ = 'players'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    position = db.Column(db.String(2), nullable=False)
    team = db.Column(db.String(50), nullable=False)
    average_draft_position = db.Column(db.Numeric(10,2), nullable=False)
    points_last_season = db.Column(db.Numeric(10,2), nullable=False)
    image_url = db.Column(db.String(225))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    rosters = db.relationship('Roster', back_populates='player', cascade='all, delete-orphan')
    draft_picks = db.relationship('DraftPick', back_populates='player', cascade='all, delete-orphan')
    trade_details = db.relationship('TradeDetail', back_populates='player', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'position': self.position,
            'team': self.team,
            'average_draft_position': self.average_draft_position,
            'points_last_season': self.points_last_season,
            'image_url': self.image_url
        }
