"""Add a column

Revision ID: ed6eecf7c143
Revises: 48589e65fa50
Create Date: 2020-01-08 14:35:27.689126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed6eecf7c143'
down_revision = '48589e65fa50'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')