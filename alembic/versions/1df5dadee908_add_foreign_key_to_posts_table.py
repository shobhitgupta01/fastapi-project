"""Add foreign key to posts table

Revision ID: 1df5dadee908
Revises: 0ec1064ac482
Create Date: 2023-01-27 16:24:08.518141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1df5dadee908'
down_revision = '0ec1064ac482'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table = 'posts', referent_table = "users",
    local_cols = ['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
