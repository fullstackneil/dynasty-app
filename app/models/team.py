from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Team(db.Model):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    league_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('leagues.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    draft_position = db.Column(db.Integer)
    image_url = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    league = db.relationship('League', back_populates='teams')
    user = db.relationship('User', back_populates='teams')
    rosters = db.relationship('Roster', back_populates='team', cascade='all, delete-orphan')
    draft_picks = db.relationship('DraftPick', back_populates='team', cascade='all, delete-orphan')
    trades = db.relationship('Trade', back_populates='offering_team', foreign_keys='Trade.offering_team_id', cascade='all, delete-orphan')
    received_trades = db.relationship('Trade', back_populates='receiving_team', foreign_keys='Trade.receiving_team_id', cascade='all, delete-orphan')
    trade_details_from = db.relationship('TradeDetail', back_populates='from_team', foreign_keys='TradeDetail.from_team_id', cascade='all, delete-orphan')
    trade_details_to = db.relationship('TradeDetail', back_populates='to_team', foreign_keys='TradeDetail.to_team_id', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'league_id': self.league_id,
            'user_id': self.user_id,
            'draft_position': self.draft_position,
            'image_url': self.image_url
        }
