from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Draft(db.Model):
    __tablename__ = 'drafts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('leagues.id')), nullable=False)
    draft_date = db.Column(db.DateTime, nullable=False)
    draft_type = db.Column(db.String(25), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    league = db.relationship('League', back_populates='drafts')
    draft_picks = db.relationship('DraftPick', back_populates='draft', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'league_id': self.league_id,
            'draft_date': self.draft_date,
            'draft_type': self.draft_type
        }
