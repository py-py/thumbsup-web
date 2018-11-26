"""proxy added count_used

Revision ID: 61db43876a0a
Revises: 3e0c7141e934
Create Date: 2018-11-26 15:30:36.582903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61db43876a0a'
down_revision = '3e0c7141e934'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proxies', sa.Column('count_used', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proxies', 'count_used')
    # ### end Alembic commands ###
