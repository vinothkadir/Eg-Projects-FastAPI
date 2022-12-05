"""add foreign-key to posts table

Revision ID: b26abf2893a5
Revises: 049ed4abd853
Create Date: 2022-12-03 20:52:44.937272

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b26abf2893a5'
down_revision = '049ed4abd853'
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
