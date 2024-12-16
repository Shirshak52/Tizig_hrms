from flask_admin.contrib.sqla import ModelView

class EmployeeAdminView(ModelView):
    # Define the columns to be shown in the list view
    column_list = ("first_name", "last_name", "department.name", "dob", "gender", "phone", "email", "emergency_contact", "address")

    # Define columns to be searchable
    column_searchable_list = ("first_name", "last_name", "email", "phone")

    # Define filters for search
    column_filters = ("department.name",)

    # Define which columns should appear on the add/edit form
    form_columns = ("first_name", "last_name", "dob", "gender", "phone", "email", "emergency_contact", "address", "department")

    column_labels = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'department.name': 'Department Name'
    }