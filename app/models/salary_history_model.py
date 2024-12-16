from app import db

class SalaryHistory(db.Model):
    __versioned__ = {
        'base_classes': (db.Model,)
    }
    __tablename__ = 'salary_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    designation_id = db.Column(db.Integer, db.ForeignKey('designations.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'), nullable=False)
    work_duration_months = db.Column(db.Integer, nullable=False)

    basic = db.Column(db.Float, nullable=False)
    allowance = db.Column(db.Float, nullable=False)
    perks_allowance = db.Column(db.Float, nullable=False)
    temp_ta = db.Column(db.Float, nullable=False)
    pf = db.Column(db.Float, nullable=False)
    net_total = db.Column(db.Float, nullable=False)  
    gross = db.Column(db.Float, nullable=False)

    # Effective date when the salary was updated
    effective_date = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(100), nullable=True, unique=False)

    # Relationships
    department = db.relationship('Department', backref='salary_history')
    designation = db.relationship('Designation', backref='salary_history')
    status = db.relationship('Status', backref='salary_history')

    def __repr__(self):
        return f"<SalaryHistory {self.id}: Employee {self.employee_id}, Status {self.status_id}>"
