"""empty message

Revision ID: 8144c7c20dc6
Revises: d2233b7d98c4
Create Date: 2019-03-12 21:09:15.746360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8144c7c20dc6'
down_revision = 'd2233b7d98c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
