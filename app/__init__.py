from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from sqlalchemy_continuum import make_versioned, version_class
from flask_admin import Admin

# Initialize addon instances
make_versioned(user_cls=None)
db = SQLAlchemy()
migrate = Migrate()
administrator = Admin(name='Tizig HR')

def create_app():
    # Create and configure the Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Explicitly state a version-tracking strategy
        # versioning_manager.strategy = 'validity'

        # Import model classes for migration
        from app.models.department_model import Department
        from app.models.designation_model import Designation
        from app.models.status_model import Status
        from app.models.employee_model import Employee
        from app.models.employee_documents_model import EmployeeDocument
        from app.models.salary_history_model import SalaryHistory

        # version_class(SalaryHistory)

        # Setup model views
        from flask_admin.contrib.sqla import ModelView
        from app.views.department_view import DepartmentAdminView
        from app.views.designation_view import DesignationAdminView
        from app.views.status_view import StatusAdminView
        from app.views.employee_view import EmployeeAdminView
        from app.views.salary_history_view import SalaryHistoryAdminView

        administrator.add_view(EmployeeAdminView(Employee, db.session))  # Set up Employee CRUD views
        administrator.add_view(DepartmentAdminView(Department, db.session))  # Set up Department CRUD views
        administrator.add_view(DesignationAdminView(Designation, db.session))  # Set up Designation CRUD views
        administrator.add_view(StatusAdminView(Status, db.session))  # Set up Status CRUD views
        administrator.add_view(SalaryHistoryAdminView(SalaryHistory, db.session))  # Set up SalaryHistory CRUD views
        administrator.add_view(ModelView(EmployeeDocument, db.session))  # Set up EmployeeDocument CRUD views
        administrator.init_app(app)

        # Register blueprints here

    return app

