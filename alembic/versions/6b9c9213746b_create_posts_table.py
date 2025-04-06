"""Create posts table

Revision ID: 6b9c9213746b
Revises: 
Create Date: 2025-04-05 20:46:50.967937

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b9c9213746b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# When we want to commit or add tables
def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable = False,primary_key=True),sa.Column('title',sa.String(),nullable=False,))
    pass

# When we want to rollback
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
