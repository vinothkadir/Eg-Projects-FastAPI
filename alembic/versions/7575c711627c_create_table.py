"""create table

Revision ID: 7575c711627c
Revises: 
Create Date: 2022-12-03 19:26:24.473921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7575c711627c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), primary_key=True, nullable=False),sa.Column('title', sa.Integer(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass
