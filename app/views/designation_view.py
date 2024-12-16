from flask_admin.contrib.sqla import ModelView

class DesignationAdminView(ModelView):
    form_columns = ('name',)
    