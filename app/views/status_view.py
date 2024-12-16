from flask_admin.contrib.sqla import ModelView

class StatusAdminView(ModelView):
    form_columns = ('name',)
    
