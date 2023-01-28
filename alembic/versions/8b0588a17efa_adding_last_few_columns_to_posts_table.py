"""Adding last few columns to posts table

Revision ID: 8b0588a17efa
Revises: 1df5dadee908
Create Date: 2023-01-28 22:03:06.587136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b0588a17efa'
down_revision = '1df5dadee908'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable = False, server_default='TRUE'),)

    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default=sa.text('NOW()')),)


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
