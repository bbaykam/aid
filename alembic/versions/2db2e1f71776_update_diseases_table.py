"""update diseases table

Revision ID: 2db2e1f71776
Revises: 763a68d20354
Create Date: 2019-12-05 22:32:22.371961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2db2e1f71776'
down_revision = '763a68d20354'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('diseases')
    op.create_table(
        'diseases',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('code', sa.String(8), nullable=False),
        sa.Column('name', sa.String(256), nullable=False),
    )


def downgrade():
    pass
