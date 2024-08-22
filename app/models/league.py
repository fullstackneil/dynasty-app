from .db import db, environment, SCHEMA, add_prefix_for_prod



class League(db.Model):
    __tablename__: 'leagues'
    
