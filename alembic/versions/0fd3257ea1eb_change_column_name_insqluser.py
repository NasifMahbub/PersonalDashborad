"""add new in SQLUser

Revision ID: 0fd3257ea1eb
Revises: c59520598f1c
Create Date: 2020-01-08 16:04:30.145256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fd3257ea1eb'
down_revision = 'c59520598f1c'
branch_labels = None
depends_on = None


def upgrade():
    """ op.a_column("users", "email_adress", new_column_name="email_address", existing_nullable = sa.false) """
    op.add_column('users', sa.Column('image', sa.String(250))
)


def downgrade():
    """ op.alter_column("users", "email_address", new_column_name="email_adress", existing_nullable = sa.false) """
    op.drop_column('users', 'image')
