from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from sqlalchemy_continuum import make_versioned
from flask_admin import Admin

# Initialize addon instances
db = SQLAlchemy()
migrate = Migrate()
administrator = Admin(name='Tizig HR Admin')

def create_app():
    # print(f"SQLALCHEMY_DATABASE_URI: {Config.SQLALCHEMY_DATABASE_URI}")

    # Create and configure the Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the app with the addons
    # make_versioned(user_cls=None) # To track data inserts/updates/deletes
                                                               # Must be done before db.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import model classes for migration
        from app.models.employee_model import Employee


        # Setup model views
        from flask_admin.contrib.sqla import ModelView
        administrator.add_view(ModelView(Employee, db.session))  # Set up Employee CRUD views
        administrator.init_app(app)


        # Register blueprints here

    return app

