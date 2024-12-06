"""Added is_admin field to User model

Revision ID: f0065aacc3e9
Revises: 
Create Date: 2024-12-07 02:02:37.135854

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f0065aacc3e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('train',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('source', sa.String(length=100), nullable=False),
    sa.Column('destination', sa.String(length=100), nullable=False),
    sa.Column('total_seats', sa.Integer(), nullable=False),
    sa.Column('available_seats', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)
        batch_op.drop_column('is_admin')

    op.drop_table('train')
    # ### end Alembic commands ###