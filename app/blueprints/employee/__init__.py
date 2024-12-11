from flask import Blueprint

employee = Blueprint('employee', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/app/blueprints/employee/static')