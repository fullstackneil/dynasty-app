from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    position = db.Column(db.String(2), nullable=False)
    team = db.Column(db.String(40), nullable=False)
    average_draft_position = db.Column(db.Numeric(2,1), nullable=False)
    points_last_season = db.Column(db.Numeric(3,1), nullable=False)
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
            'points_last_season': self.points_last_season
        }
