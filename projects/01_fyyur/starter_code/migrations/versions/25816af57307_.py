"""Create 'artists' table

Revision ID: 25816af57307
Revises: 0957757dc0c9
Create Date: 2021-04-26 18:22:52.850866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25816af57307'
down_revision = '0957757dc0c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('city', sa.String(length=120), nullable=True),
        sa.Column('state', sa.String(length=120), nullable=True),
        sa.Column('phone', sa.String(length=120), nullable=True),
        sa.Column('genres', sa.String(), nullable=True),
        sa.Column('image_link', sa.String(length=500), nullable=True),
        sa.Column('facebook_link', sa.String(length=120), nullable=True),
        sa.Column('seeking_venue', sa.Boolean(), nullable=True),
        sa.Column('seeking_description', sa.String(length=500), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    # ### populate database with test data ###
    # op.execute("INSERT INTO artists (id, name, city, state, phone, seeking_venue, seeking_description) VALUES (1, 'Matthieu Arnaud', 'Paris', 'IDF', '+33 1 60 33 06 03', True, 'Je cherche une scène hebdomadaire')")
    # op.execute("INSERT INTO artists (id, name, city, seeking_venue, seeking_description) VALUES (2, 'Jorge Drexler', 'Montevideo', False, 'Madrid es suficiente...')")
    # op.execute("INSERT INTO artists (id, name, city) VALUES (3, 'Apt Punk', 'unknown')")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artists')
    # ### end Alembic commands ###
