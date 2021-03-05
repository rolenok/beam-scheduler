"""empty message

Revision ID: 3489cb4f8ca9
Revises: b6c6d3265dfb
Create Date: 2020-10-21 15:26:56.489448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3489cb4f8ca9'
down_revision = 'b6c6d3265dfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('request', 'day_of_month')
    op.drop_column('request', 'start_time')
    op.drop_column('request', 'end_time')
    op.add_column('user', sa.Column('priority', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'priority')
    op.add_column('request', sa.Column('end_time', sa.INTEGER(), nullable=True))
    op.add_column('request', sa.Column('start_time', sa.INTEGER(), nullable=True))
    op.add_column('request', sa.Column('day_of_month', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
