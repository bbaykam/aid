"""create diseases table

Revision ID: 0853699e1569
Revises:
Create Date: 2019-10-25 13:59:02.346270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0853699e1569'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'diseases',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('IDC_10', sa.String(15), nullable=False),
        sa.Column('disease', sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table('diseases')
