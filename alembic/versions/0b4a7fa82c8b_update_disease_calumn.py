"""update disease calumn

Revision ID: 0b4a7fa82c8b
Revises: 0853699e1569
Create Date: 2019-12-04 12:46:12.714532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b4a7fa82c8b'
down_revision = '0853699e1569'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('diseases', 'disease')
    op.add_column('diseases', sa.Column('disease', sa.String(256), nullable=False))



def downgrade():
    pass
