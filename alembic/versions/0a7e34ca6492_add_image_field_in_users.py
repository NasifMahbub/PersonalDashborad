"""add image field in users

Revision ID: 0a7e34ca6492
Revises: c9d1e4e34553
Create Date: 2020-01-15 15:29:30.346205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a7e34ca6492'
down_revision = 'c9d1e4e34553'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("image_url", sa.String(512)))


def downgrade():
    op.drop_column("users", "image_url")
