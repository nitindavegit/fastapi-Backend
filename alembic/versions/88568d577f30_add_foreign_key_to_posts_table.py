"""add foreign key to posts table

Revision ID: 88568d577f30
Revises: 5eefccb704ef
Create Date: 2025-04-05 21:31:22.496891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88568d577f30'
down_revision: Union[str, None] = '5eefccb704ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',
                  sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column(("posts",'owner_id'))
    pass
