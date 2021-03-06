"""users table

Revision ID: a1d70415275e
Revises: 
Create Date: 2020-01-19 18:53:30.413181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1d70415275e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first', sa.String(length=200), nullable=True),
    sa.Column('last', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password_hash', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_first'), 'user', ['first'], unique=False)
    op.create_index(op.f('ix_user_last'), 'user', ['last'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_last'), table_name='user')
    op.drop_index(op.f('ix_user_first'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
