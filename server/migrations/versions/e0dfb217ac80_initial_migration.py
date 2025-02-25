"""Initial migration

Revision ID: e0dfb217ac80
Revises: dac4c963f1f4
Create Date: 2025-02-25 12:48:26.332306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0dfb217ac80'
down_revision = 'dac4c963f1f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('users')
    op.drop_table('articles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('author', sa.VARCHAR(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('preview', sa.VARCHAR(), nullable=False),
    sa.Column('minutes_to_read', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
