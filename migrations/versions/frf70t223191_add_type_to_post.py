"""add columns to user

Revision ID: frf70t223191
Revises: 240d251d908b
Create Date: 2017-12-21 12:34:05.816547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'frf70t223191'
down_revision = 'df2d748947ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('article_type', sa.String(), default='python'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'article_type')
    # ### end Alembic commands ###
