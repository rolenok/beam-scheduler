"""empty message

Revision ID: fa4cfba64647
Revises: 718bc4d05640
Create Date: 2020-10-08 21:27:04.663350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa4cfba64647'
down_revision = '718bc4d05640'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_request_scheduled_end'), 'request', ['scheduled_end'], unique=False)
    op.create_index(op.f('ix_request_scheduled_start'), 'request', ['scheduled_start'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_request_scheduled_start'), table_name='request')
    op.drop_index(op.f('ix_request_scheduled_end'), table_name='request')
    # ### end Alembic commands ###