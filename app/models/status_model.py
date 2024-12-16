from app import db
from sqlalchemy.types import Enum

class Status(db.Model):
    __tablename__ = 'statuses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(Enum('Probation', 'Confirmed', 'Scale Revised', name='status_types'), nullable=False, unique=True)

    def __repr__(self):
        return f"<Status {self.id}: {self.name}>"
