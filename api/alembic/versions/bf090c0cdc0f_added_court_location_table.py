"""added_court_location_table

Revision ID: bf090c0cdc0f
Revises: e15dc8fa858a
Create Date: 2021-12-28 13:53:25.425765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf090c0cdc0f'
down_revision = 'e15dc8fa858a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('court_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('short_description', sa.String(), nullable=True),
    sa.Column('location_code', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('address_line1', sa.String(), nullable=True),
    sa.Column('address_line2', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('province', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_court_location_id'), 'court_location', ['id'], unique=False)
    op.create_index(op.f('ix_court_location_name'), 'court_location', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_court_location_name'), table_name='court_location')
    op.drop_index(op.f('ix_court_location_id'), table_name='court_location')
    op.drop_table('court_location')
    # ### end Alembic commands ###
