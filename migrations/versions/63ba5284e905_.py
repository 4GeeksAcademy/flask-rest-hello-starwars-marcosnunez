"""empty message

Revision ID: 63ba5284e905
Revises: 
Create Date: 2025-01-31 20:23:34.526463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ba5284e905'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=50), nullable=False),
    sa.Column('surface_water', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('mlgt', sa.String(length=50), nullable=False),
    sa.Column('consumables', sa.String(length=50), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=False),
    sa.Column('crew', sa.String(length=5000), nullable=False),
    sa.Column('hyperdrive_rating', sa.Integer(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.Integer(), nullable=False),
    sa.Column('passengers', sa.String(length=5000), nullable=False),
    sa.Column('model', sa.String(length=5000), nullable=False),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=False),
    sa.Column('starship_class', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('home_world', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=50), nullable=False),
    sa.Column('eye_color', sa.String(length=50), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=5000), nullable=False),
    sa.ForeignKeyConstraint(['home_world'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('Planets', 'Character', 'Starships', name='favoritetypeenum'), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favourite')
    op.drop_table('character')
    op.drop_table('user')
    op.drop_table('starships')
    op.drop_table('planets')
    # ### end Alembic commands ###
