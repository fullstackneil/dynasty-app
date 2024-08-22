from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class DraftPick(db.Model):
    __tablename__ = 'draft_picks'

    id = db.Column(db.Integer, primary_key=True)
    draft_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('drafts.id')), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('players.id')), nullable=False)
    round = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    draft = db.relationship('Draft', back_populates='draft_picks')
    team = db.relationsihp('Team', back_populates='draft_picks')
    player = db.relationship('Player', back_populates='draft_picks')

    def to_dict(self):
        return {
            'id': self.id,
            'draft_id': self.draft_id,
            'team_id': self.team_id,
            'player_id': self.player_id,
            'round': self.round,
            'pick_number': self.pick_number,
        }
