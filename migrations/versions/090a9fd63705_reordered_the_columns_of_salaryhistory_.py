"""Reordered the columns of SalaryHistory model

Revision ID: 090a9fd63705
Revises: c04c065f86fc
Create Date: 2024-12-17 17:07:28.603421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090a9fd63705'
down_revision = 'c04c065f86fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee_documents', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'employees', ['employee_id'], ['id'], use_alter=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee_documents', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###