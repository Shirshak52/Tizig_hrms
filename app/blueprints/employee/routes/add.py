"""Routes for adding employee records."""

from flask import redirect, render_template, request, url_for
from app.blueprints.employee import employee
from app import db
from app.blueprints.employee.forms.employee_form import EmployeeForm
from app.models.employee_model import Employee

@employee.route('/add', methods=['GET', 'POST'])
def add_employee():
    """Route for rendering and handling the add employee form."""

    form = EmployeeForm()  # Create the Employee form linked to the Employee model

    # Validate the form after submission
    if request.method == 'POST' and form.validate_on_submit():
        new_employee = form.populate_obj(Employee())
        # print(new_employee)
        db.session.add(new_employee)
        db.session.commit()

        return redirect(url_for('employee.read'))

    # Pass to and render the form with the add employee page
    return render_template('add_employee_page.html', form=form)

