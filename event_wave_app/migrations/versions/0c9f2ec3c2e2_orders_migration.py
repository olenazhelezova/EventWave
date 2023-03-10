"""Orders migration

Revision ID: 0c9f2ec3c2e2
Revises: 36d4b382a408
Create Date: 2023-03-02 17:02:54.961222

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0c9f2ec3c2e2'
down_revision = '36d4b382a408'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=False))
        batch_op.drop_column('cost')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cost', mysql.DECIMAL(precision=10, scale=2), nullable=False))
        batch_op.drop_column('price')

    # ### end Alembic commands ###
