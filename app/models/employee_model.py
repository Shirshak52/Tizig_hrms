from datetime import date
from app import db
from sqlalchemy.types import Enum
from sqlalchemy.orm import validates

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(Enum('Male', 'Female', name='gender_types'), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    emergency_contact = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    # Relationships
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    department = db.relationship('Department', backref='employees')

    # Relationship to SalaryHistory
    salary_history = db.relationship('SalaryHistory', backref='employee', lazy='dynamic')

    def __repr__(self):
        return f"<Employee {self.id}: {self.first_name} {self.last_name}>"
    