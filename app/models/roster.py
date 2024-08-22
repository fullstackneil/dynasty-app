from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Roster(db.Model):
    __tablename__ = 'rosters'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('players.id')), nullable=False)
    position_slot = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    team = db.relationship('Team', back_populates='rosters')
    player = db.relationship('Player', back_populates='rosters')

    def to_dict(self):
        return {
            'id': self.id,
            'team_id': self.team_id,
            'player_id': self.player_id,
            'position_slot': self.position_slot,
        }
