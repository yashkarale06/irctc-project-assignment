"""Add booking model

Revision ID: 70adc55112b6
Revises: f0065aacc3e9
Create Date: 2024-12-07 02:43:05.362002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70adc55112b6'
down_revision = 'f0065aacc3e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('train_id', sa.Integer(), nullable=False),
    sa.Column('seat_number', sa.Integer(), nullable=False),
    sa.Column('booking_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['train_id'], ['train.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    # ### end Alembic commands ###
