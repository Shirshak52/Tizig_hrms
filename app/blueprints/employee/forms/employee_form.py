"""Form for entering employee data."""

from wtforms import SubmitField, SelectField
from app.forms.base_modelform import ModelForm
from app.models.employee_model import Employee

class EmployeeForm(ModelForm):
    """Form for creating and editing employee records."""
    class Meta:
        model = Employee  # Set the SQLAlchemy database model class

        # Map Employee model attributes to suitable form input labels
        field_args = {
            'first_name': {'label': 'First Name'},
            'last_name': {'label': 'Last Name'},
            'dob': {'label': 'Date of Birth'},
            'marital_status': {'label': 'Marital Status'},
            'gender': {'label': 'Gender'},
            'phone': {'label': 'Phone Number'},
            'email': {'label': 'Email Address'},
            'emergency_contact': {'label': 'Emergency Contact'},
            'address': {'label': 'Address'}
        }

    gender = SelectField(choices=[('Male', 'Male'), ('Female', 'Female')], coerce=str)
    marital_status = SelectField(choices=[('Single', 'Single'), ('Married', 'Married')], coerce=str)
    submit = SubmitField('Submit')
