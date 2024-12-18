from app import db

class Designation(db.Model):
    __tablename__ = 'designations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    salary_histories = db.relationship('SalaryHistory', back_populates='designation', lazy=True)

    def __repr__(self):
        return f"<Designation {self.id}: {self.name}>"
