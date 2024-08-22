from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class TradeDetail(db.Model):
    __tablename__ = 'trade_details'

    id = db.Column(db.Integer, primary_key=True)
    trade_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('trades.id')), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('players.id')), nullable=False)
    from_team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    to_team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    trade = db.relationship('Trade', back_populates='trade_details')
    player = db.relationship('Player', back_populates='trade_details')
    from_team = db.relationship('Team', back_populates='trade_details_from', foreign_keys=[from_team_id])
    to_team = db.relationship('Team', back_populates='trade_details_to', foreign_keys=[to_team_id])


    def to_dict(self):
        return {
            'id': self.id,
            'trade_id': self.trade_id,
            'player_id': self.player_id,
            'from_team_id': self.from_team_id,
            'to_team_id': self.to_team_id
        }
