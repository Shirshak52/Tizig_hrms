from app import db

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    employees = db.relationship('Employee', back_populates='department', lazy=True)
    salary_histories = db.relationship('SalaryHistory', back_populates='department', lazy=True)


    def __repr__(self):
        return f"<Department {self.id}: {self.name}>"
