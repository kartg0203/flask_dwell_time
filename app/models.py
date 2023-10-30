from .extensions import db
from sqlalchemy.dialects.postgresql import JSONB


class TalcDwellTime(db.Model):
    __tablename__ = 'talc_dwell_time'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    start_timestamp = db.Column(db.Integer)
    end_timestamp = db.Column(db.Integer, nullable=True)
    event = db.Column(JSONB, nullable=True)
