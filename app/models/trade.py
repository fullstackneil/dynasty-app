from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Trade(db.Model):
    __tablename__ = 'trades'

    id = db.Column(db.Integer, primary_key=True)
    offering_team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    receiving_team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    offering_team = db.relationship('Team', back_populates='trades', foreign_keys=[offering_team_id])
    receiving_team = db.relationship('Team', back_populates='received_trades', foreign_keys=[receiving_team_id])
    trade_details = db.relationship('TradeDetail', back_populates='trade', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'offering_team_id': self.offering_team_id,
            'receiving_team_id': self.receiving_team_id,
            'status': self.status
        }
