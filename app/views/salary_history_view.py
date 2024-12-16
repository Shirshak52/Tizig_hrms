from flask_admin.contrib.sqla import ModelView

# SalaryHistory CRUD View (Main View)
class SalaryHistoryVersionAdminView(ModelView):
    column_list = ('id', 
                   'employee.first_name', 
                   'employee.last_name', 
                   'department.name', 
                   'designation.name', 
                   'status.name', 
                   'basic', 
                   'allowance', 
                   'perks_allowance', 
                   'temp_ta', 
                   'pf', 
                   'net_total', 
                   'gross', 
                   'effective_date', 
                   'remarks')
    
    column_searchable_list = ('employee.first_name', 'employee.last_name')
    column_filters = ('department.name', 'designation.name', 'status.name')

    
    # Custom column labels to display in the UI
    column_labels = {
        'employee.first_name': 'Employee First Name',
        'employee.last_name': 'Employee Last Name',
        'department.name': 'Department Name',
        'designation.name': 'Designation Name',
        'status.name': 'Status Name',
        'basic': 'Basic Salary',
        'allowance': 'Allowance',
        'perks_allowance': 'Perks Allowance',
        'temp_ta': 'Temp TA',
        'pf': 'PF',
        'net_total': 'Net Total',
        'gross': 'Gross Salary',
        'effective_date': 'Effective Date'
    }

    form_excluded_columns = ('transaction_id', 
                    'operation_type', 
                    'designation', 
                    'status', 
                    'basic', 
                    'allowance', 
                    'perks_allowance', 
                    'temp_ta', 
                    'pf', 
                    'net_total', 
                    'gross', 
                    'effective_date', 
                    'remarks')
    

    def get_query(self):
        return self.session.query(self.model).order_by(
            self.model.employee_id, 
            self.model.effective_date.desc()
        )
    
    def get_count_query(self):
        return self.session.query(self.model).count()