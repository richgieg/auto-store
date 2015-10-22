"""Remove year field from automobiles

Revision ID: 5ad1f9ba378e
Revises: 395cec770df2
Create Date: 2015-10-22 00:49:05.990505

"""

# revision identifiers, used by Alembic.
revision = '5ad1f9ba378e'
down_revision = '395cec770df2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('automobiles', 'year')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('automobiles', sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=False))
    ### end Alembic commands ###