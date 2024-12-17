from datetime import date
from flask import request
from flask_admin.contrib.sqla import ModelView

# SalaryHistory CRUD View (Main View)
class SalaryHistoryAdminView(ModelView):
    column_list = ('employee.first_name', 
                   'employee.last_name', 
                   'department.name', 
                   'designation.name', 
                   'status.name',
                   "start_date",
                   "end_date",
                   "work_duration",
                   'basic', 
                   'allowance', 
                   'perks_allowance', 
                   'temp_ta', 
                   'pf', 
                   'net_total', 
                   'gross', 
                   'remarks')
    
    column_searchable_list = ('employee.first_name', 'employee.last_name')
    column_filters = ('department.name', 'designation.name', 'status.name')
    column_group_labels = ('employee.first_name', 'designation.name')


    # Custom column labels to display in the UI
    column_labels = {
        'employee.first_name': 'Employee First Name',
        'employee.last_name': 'Employee Last Name',
        'department.name': 'Department',
        'designation.name': 'Designation',
        'status.name': 'Status',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'work_duration': 'Work Duration (Days)',
        'basic': 'Basic Salary',
        'allowance': 'Allowance',
        'perks_allowance': 'Perks Allowance',
        'temp_ta': 'Temp TA',
        'pf': 'PF',
        'net_total': 'Net Total',
        'gross': 'Gross Salary',
        'effective_date': 'Effective Date'
    }

    form_columns = ("employee",
                    "designation",
                    "status",
                    "start_date",
                    "end_date",
                    "basic",
                    "allowance",
                    "perks_allowance",
                    "temp_ta",
                    "net_total",
                    "pf",
                    "gross",
                    "remarks"
                    )
    
    def _work_duration_formatter(view, context, model, name):
        if model.end_date:
            return (model.end_date - model.start_date).days
        return (date.today() - model.start_date).days
    
    column_formatters = { 'work_duration': _work_duration_formatter }

    # def get_query(self):
    #     return self.session.query(self.model).order_by(
    #         self.model.employee_id, 
    #         self.model.effective_date.desc()
    #     )
    
    # def get_count_query(self):
    #     return self.session.query(self.model).count()