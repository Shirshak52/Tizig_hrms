from app import db
from app.models.employee_model import Employee
from sqlalchemy import event

class SalaryHistory(db.Model):
    __versioned__ = {
        # 'base_classes': (db.Model,)
    }
    __tablename__ = 'salary_history'

    # Composite primary key
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), primary_key=True, nullable=False)
    job_category_id = db.Column(db.Integer, db.ForeignKey('job_categories.id'), primary_key=True, nullable=False)
    designation_id = db.Column(db.Integer, db.ForeignKey('designations.id'), primary_key=True, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'), primary_key=True, nullable=False)

    # Start and end dates of each status
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)

    # Salary details
    basic = db.Column(db.Float, nullable=False)
    allowance = db.Column(db.Float, nullable=False)
    perks_allowance = db.Column(db.Float, nullable=False)
    temp_ta = db.Column(db.Float, nullable=False)
    net_total = db.Column(db.Float, nullable=False)
    pf = db.Column(db.Float, nullable=False)
    gross = db.Column(db.Float, nullable=False)

    # Remarks
    remarks = db.Column(db.String(100), nullable=True, unique=False)

    # Relationships
    department = db.relationship('Department', back_populates='salary_histories')
    job_category = db.relationship('JobCategory', back_populates='salary_histories')
    designation = db.relationship('Designation', back_populates='salary_histories')
    status = db.relationship('Status', back_populates='salary_histories')
    employee = db.relationship('Employee', back_populates='salary_histories')

    def __repr__(self):
        return f"<SalaryHistory {self.id}: Employee {self.employee_id}, Status {self.status_id}>"
    
# Function to set department_id based on employee_id
def set_department_id(mapper, connection, target):
    employee = db.session.query(Employee).get(target.employee_id)
    if employee:
        target.department_id = employee.department_id

event.listen(SalaryHistory, 'before_insert', set_department_id)
event.listen(SalaryHistory, 'before_update', set_department_id)
    