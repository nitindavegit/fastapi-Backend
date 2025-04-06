"""add content column to posts table

Revision ID: b5e63b97ee9d
Revises: 6b9c9213746b
Create Date: 2025-04-05 21:12:21.882678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5e63b97ee9d'
down_revision: Union[str, None] = '6b9c9213746b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
