"""meetups model

Revision ID: 1bfef46a5e74
Revises: 
Create Date: 2019-09-16 01:32:03.338311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bfef46a5e74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('happeningOn', sa.DateTime(), nullable=True),
    sa.Column('createdOn', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meetup')
    # ### end Alembic commands ###
