"""add last few columns to post table

Revision ID: e5cfb142b8ba
Revises: 88568d577f30
Create Date: 2025-04-05 21:47:06.203731

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5cfb142b8ba'
down_revision: Union[str, None] = '88568d577f30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',
                  sa.Column(
                      'published',sa.Boolean(),nullable=False,server_default='True'),)
    
    op.add_column('posts',
                  sa.Column(
                        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
