from app import db
from sqlalchemy.types import Enum

class Status(db.Model):
    __tablename__ = 'statuses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(Enum('Trainee', 'Probation', 'Confirmed', 'Scale Revised', name='status_types'), 
                     nullable=False, unique=True)
    
    # Relationships
    salary_histories = db.relationship('SalaryHistory', back_populates='status', lazy=True)


    def __repr__(self):
        return f"<Status {self.id}: {self.name}>"
