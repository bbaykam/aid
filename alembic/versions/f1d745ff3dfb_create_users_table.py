"""create users table

Revision ID: f1d745ff3dfb
Revises: a3d04c5a6839
Create Date: 2019-12-17 17:49:08.095161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1d745ff3dfb'
down_revision = 'a3d04c5a6839'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(63), nullable=False),
        sa.Column('last_name', sa.String(63), nullable=False),
        sa.Column('birth_date', sa.Date, nullable=False),
        sa.Column('gender', sa.Enum('male', 'female', name='gender'), nullable=False),
        sa.Column('email', sa.String(63), nullable=False, unique=True),
        sa.Column('password', sa.String(63), nullable=False),
        sa.Column('citizen_id', sa.String(30), nullable=True),
    )


def downgrade():
    op.drop_table('users')
