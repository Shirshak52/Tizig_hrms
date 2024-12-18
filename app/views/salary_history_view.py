from datetime import date
from flask import request
from flask_admin.contrib.sqla import ModelView
from wtforms import ValidationError
from app import db
from app.models.salary_history_model import SalaryHistory

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

    # Check for validity after form is submitted
    def on_model_change(self, form, model, is_created):
        # If start date is later than end date, raise error
        if model.end_date and model.start_date > model.end_date:
            raise ValidationError("Start Date cannot be after End Date.")
        
        # When inserting a new record, ensure start date > latest end date for same employee
        # When updating an existing record, ensure that start date > previous (second-latest) end date
        if model.employee_id:
            # When inserting
            if is_created:
                latest_salary = db.session.query(SalaryHistory).filter_by(employee_id=model.employee_id).order_by(SalaryHistory.end_date.desc()).first()
                if latest_salary and model.start_date <= latest_salary.end_date:
                    raise ValidationError(f"Start Date must be after the latest End Date ({latest_salary.end_date}) for this employee.")
            
            # When updating
            else:
                # Get the two latest records ordered by end date
                latest_salary = db.session.query(SalaryHistory).filter_by(employee_id=model.employee_id).order_by(SalaryHistory.end_date.desc()).limit(2).all()

                # If there are more than 1 entries for the same employee
                if len(latest_salary) > 1:
                    # Second latest end date
                    second_latest_end_date = latest_salary[1].end_date
                    if model.start_date <= second_latest_end_date:
                        raise ValidationError(f"Start Date must be after the previous End Date ({second_latest_end_date}) for this employee.")
                
                # If there is only 1 entry for an employee
                elif len(latest_salary) == 1:
                    # If there's only one existing record, we compare with the latest end date
                    latest_end_date = latest_salary[0].end_date
                    if model.start_date <= latest_end_date:
                        raise ValidationError(f"Start Date must be after the latest End Date ({latest_end_date}) for this employee.")

        
        # When inserting a new record,
        # ensure the employee, designation, and status combo do not match existing ones

        # Get existing records for an employee
        existing_salary = db.session.query(SalaryHistory).filter_by(
            employee_id=model.employee_id,
            designation_id=model.designation_id,
            status_id=model.status_id
        ).first()

        if existing_salary:
            # If updating the same record, skip validation check
            if not is_created and existing_salary.employee_id == model.employee_id and existing_salary.designation_id == model.designation_id and existing_salary.status_id == model.status_id and existing_salary.start_date == model.start_date:
                pass
            else:
                raise ValidationError("This combination of Employee, Designation, and Status already exists.")

        return super(SalaryHistoryAdminView, self).on_model_change(form, model, is_created)