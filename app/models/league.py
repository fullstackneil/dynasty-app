from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime



class League(db.Model):
    __tablename__ = 'leagues'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    commissioner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    draft_type = db.Column(db.String(20))
    scoring_system = db.Column(db.String(20))
    max_teams = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    commissioner = db.relationship('User', back_populates='leagues')
    drafts = db.relationship('Draft', back_populates='league', cascade='all, delete-orphan')
    teams = db.relationship('Team', back_populates='league', cascade='all, delete-orphan')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'commissioner_id': self.comissioner_id,
            'draft_type': self.draft_type,
            'scoring_system': self.scoring_system,
            'max_teams': self.max_teams,
        }
