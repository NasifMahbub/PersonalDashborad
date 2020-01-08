"""create account table

Revision ID: 48589e65fa50
Revises: 
Create Date: 2020-01-08 12:46:04.575488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48589e65fa50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')