"""add content column to post table

Revision ID: afa1e9a8379b
Revises: 7575c711627c
Create Date: 2022-12-03 19:42:59.323677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afa1e9a8379b'
down_revision = '7575c711627c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column('posts','content')
    pass
