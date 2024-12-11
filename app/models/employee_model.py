from sqlalchemy.types import Enum
from sqlalchemy_continuum import make_versioned, version_class
from app import db

# make_versioned(user_cls=None)

class Employee(db.Model):
    __versioned__ = {}  # To track data inserts/updates/deletes
    __tablename__ = 'employees'  # Table name in the database

    # Primary key for the employee record
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Employee personal details
    first_name = db.Column(db.String(50), nullable=False)  # First name
    last_name = db.Column(db.String(50), nullable=False)  # Last name
    dob = db.Column(db.Date, nullable=False)  # Date of birth
    marital_status = db.Column(Enum('Single', 'Married', 'Divorced', 'Widowed', name='marital_status'),
                               nullable=False)  # Marital status
    gender = db.Column(Enum('Male', 'Female', name='gender'), nullable=False)  # Gender
    phone = db.Column(db.String(15), nullable=False)  # Phone number
    email = db.Column(db.String(100), nullable=False, unique=True)  # Email address (unique constraint)
    emergency_contact = db.Column(db.String(15), nullable=False)  # Emergency contact number
    address = db.Column(db.String(200), nullable=False)  # Physical address

    def __repr__(self):
        return f"<Employee {self.employee_id}: {self.first_name} {self.last_name}>"

# print("Employee model initialized:", Employee)
# print("Is Employee versioned before calling version_class:", hasattr(Employee, '__versioned__'))

# Enable versioning for Employee entity
# version_class(Employee)
