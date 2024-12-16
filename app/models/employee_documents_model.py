from app import db

class EmployeeDocument(db.Model):
    __tablename__ = 'employee_documents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id', use_alter=True), nullable=False)
    document_type = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationship
    employee = db.relationship('Employee', backref='documents')

    def __repr__(self):
        return f"<Document {self.id} for Employee {self.employee_id}>"
