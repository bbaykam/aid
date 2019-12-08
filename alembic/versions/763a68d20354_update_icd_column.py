"""update icd column

Revision ID: 763a68d20354
Revises: 0b4a7fa82c8b
Create Date: 2019-12-05 15:34:01.832006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '763a68d20354'
down_revision = '0b4a7fa82c8b'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('diseases', 'IDC_10')
    op.add_column('diseases', sa.Column('icd_code', sa.String(8), nullable=False))



def downgrade():
    pass
