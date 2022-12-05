"""add phone number

Revision ID: 032497d094d9
Revises: e7a972ff5d0d
Create Date: 2022-12-04 19:40:05.812436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '032497d094d9'
down_revision = 'e7a972ff5d0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'phone_number')
    # ### end Alembic commands ###
