"""Added hashed_password

Revision ID: 8abadac669c4
Revises: 927a9da59d15
Create Date: 2024-08-31 14:29:12.194490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8abadac669c4'
down_revision = '927a9da59d15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hashed_password', sa.String(length=35), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=30), nullable=False))
        batch_op.drop_column('hashed_password')

    # ### end Alembic commands ###
