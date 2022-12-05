"""add user table

Revision ID: 049ed4abd853
Revises: afa1e9a8379b
Create Date: 2022-12-03 19:54:31.076759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '049ed4abd853'
down_revision = 'afa1e9a8379b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
    pass

def downgrade():
    op.drop_table('users')
    pass
