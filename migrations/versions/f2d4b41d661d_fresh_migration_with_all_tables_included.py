"""Fresh migration with all tables included

Revision ID: f2d4b41d661d
Revises: 
Create Date: 2024-12-16 14:52:50.003863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2d4b41d661d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('designations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employee_documents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('document_type', sa.String(length=100), nullable=False),
    sa.Column('file_path', sa.String(length=200), nullable=False),
    sa.Column('uploaded_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statuses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Enum('Probation', 'Confirmed', 'Scale Revised', name='status_types'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('gender', sa.Enum('Male', 'Female', name='gender_types'), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('emergency_contact', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=False),
    sa.Column('designation_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['designation_id'], ['designations.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('salary_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('basic', sa.Float(), nullable=False),
    sa.Column('allowance', sa.Float(), nullable=False),
    sa.Column('perks_allowance', sa.Float(), nullable=False),
    sa.Column('temp_ta', sa.Float(), nullable=False),
    sa.Column('net_total', sa.Float(), nullable=False),
    sa.Column('provident_fund', sa.Float(), nullable=False),
    sa.Column('gross', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salary_details')
    op.drop_table('employees')
    op.drop_table('statuses')
    op.drop_table('employee_documents')
    op.drop_table('designations')
    op.drop_table('departments')
    # ### end Alembic commands ###
