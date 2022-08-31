"""initial db

Revision ID: 842bc0f3997c
Revises: 
Create Date: 2022-08-29 21:57:22.591277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '842bc0f3997c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URL_map',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original', sa.String(length=256), nullable=False),
    sa.Column('short', sa.String(length=16), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('URL_map')
    # ### end Alembic commands ###