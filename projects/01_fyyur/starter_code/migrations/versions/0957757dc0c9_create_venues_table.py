"""Create 'venues' table

Revision ID: 0957757dc0c9
Revises: 
Create Date: 2021-04-22 13:40:43.093488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0957757dc0c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### create 'venues' table ###
    op.create_table('venues',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('genres', sa.String(), nullable=True),
        sa.Column('city', sa.String(length=120), nullable=True),
        sa.Column('state', sa.String(length=120), nullable=True),
        sa.Column('address', sa.String(length=120), nullable=True),
        sa.Column('phone', sa.String(length=120), nullable=True),
        sa.Column('website_link', sa.String(length=120), nullable=True),
        sa.Column('image_link', sa.String(length=500), nullable=True),
        sa.Column('facebook_link', sa.String(length=120), nullable=True),
        sa.Column('seeking_talent', sa.Boolean(), nullable=True),
        sa.Column('seeking_description', sa.String(length=500), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # ### populate database with test data ###
    op.execute("INSERT INTO venues (id, name, city, state, address, phone, seeking_talent, seeking_description) VALUES (1, 'Le Piano Vache', 'Paris', 'IDF', '8 rue Laplace', '+33 1 46 33 75 03', True, 'Nous cherchons des artist-e-s pour quand la pandemie soit finie ! Contactez-nous !')")
    op.execute("INSERT INTO venues (id, name, city, state, address, phone, website_link, seeking_talent) VALUES (2, 'Teatro Colón', 'Buenos Aires', 'CABA', 'Cerrito 628', '+54 11 4378 7100', 'https://www.teatrocolon.org.ar/', False)")
    op.execute("INSERT INTO venues (id, name, address, website_link, phone, seeking_talent) VALUES (3, 'Cirque du Soleil', 'itinerant', 'https://www.cirquedusoleil.com/', '+1 877 924 7783', False)")

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venues')
    # ### end Alembic commands ###
