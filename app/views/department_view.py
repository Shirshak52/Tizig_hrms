from flask_admin.contrib.sqla import ModelView

class DepartmentAdminView(ModelView):
    form_columns = ('name',)

