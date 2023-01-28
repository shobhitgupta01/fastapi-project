"""Add content column to posts table

Revision ID: 99eeb7d189c2
Revises: 90d5c4ac02c7
Create Date: 2023-01-27 14:53:38.359625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99eeb7d189c2'
down_revision = '90d5c4ac02c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
