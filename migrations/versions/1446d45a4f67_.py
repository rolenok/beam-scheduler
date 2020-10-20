"""empty message

Revision ID: 1446d45a4f67
Revises: fa4cfba64647
Create Date: 2020-10-08 21:32:52.234973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1446d45a4f67'
down_revision = 'fa4cfba64647'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('day_of_month', sa.Integer(), nullable=True))
    op.add_column('request', sa.Column('end_time', sa.Integer(), nullable=True))
    op.add_column('request', sa.Column('is_maintenance', sa.Boolean(), nullable=True))
    op.add_column('request', sa.Column('start_time', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_request_day_of_month'), 'request', ['day_of_month'], unique=False)
    op.create_index(op.f('ix_request_end_time'), 'request', ['end_time'], unique=False)
    op.create_index(op.f('ix_request_is_maintenance'), 'request', ['is_maintenance'], unique=False)
    op.create_index(op.f('ix_request_start_time'), 'request', ['start_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_request_start_time'), table_name='request')
    op.drop_index(op.f('ix_request_is_maintenance'), table_name='request')
    op.drop_index(op.f('ix_request_end_time'), table_name='request')
    op.drop_index(op.f('ix_request_day_of_month'), table_name='request')
    op.drop_column('request', 'start_time')
    op.drop_column('request', 'is_maintenance')
    op.drop_column('request', 'end_time')
    op.drop_column('request', 'day_of_month')
    # ### end Alembic commands ###
