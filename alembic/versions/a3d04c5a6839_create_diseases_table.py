"""create diseases table

Revision ID: a3d04c5a6839
Revises:
Create Date: 2019-12-17 17:46:57.888942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3d04c5a6839'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'diseases',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('code', sa.String(8), nullable=False),
        sa.Column('name', sa.String(256), nullable=False),
    )


def downgrade():
    op.drop_table('diseases')
