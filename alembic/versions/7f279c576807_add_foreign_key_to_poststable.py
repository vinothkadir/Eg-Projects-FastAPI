"""add foreign-key to poststable

Revision ID: 7f279c576807
Revises: b26abf2893a5
Create Date: 2022-12-04 19:13:39.158895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f279c576807'
down_revision = 'b26abf2893a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass

def downgrade():
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
