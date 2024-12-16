from app import db

class SalaryDetails(db.Model):
    __tablename__ = 'salary_details'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)

    basic = db.Column(db.Float, nullable=False)
    allowance = db.Column(db.Float, nullable=False)
    perks_allowance = db.Column(db.Float, nullable=False)
    temp_ta = db.Column(db.Float, nullable=False)
    net_total = db.Column(db.Float, nullable=False)
    provident_fund = db.Column(db.Float, nullable=False)
    gross = db.Column(db.Float, nullable=False)

    # Relationship
    employee = db.relationship('Employee', backref='salary_details')

    def __repr__(self):
        return f"<SalaryDetails for Employee {self.employee_id}>"
