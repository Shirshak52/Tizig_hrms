from app import db
from sqlalchemy.types import Enum

class JobCategory(db.Model):
    __tablename__ = 'job_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(Enum('Technical', 'Non-technical', name='job_category_types'), 
                     nullable=False, unique=True)
    
    # Relationships
    employees = db.relationship('Employee', back_populates='job_category', lazy=True)
    salary_histories = db.relationship('Employee', back_populates='job_category', lazy=True)


    def __repr__(self):
        return f"<Job Category {self.id}: {self.name}>"
