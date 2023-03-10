"""making changes

Revision ID: 7e5844a6ced5
Revises: 
Create Date: 2023-02-28 19:36:58.438360

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7e5844a6ced5'
down_revision = None
branch_labels = ('default',)
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('geoDatas',
    sa.Column('data_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('vehicle_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('altimeter', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('data_id')
    )
    op.create_table('telemetryDatas',
    sa.Column('data_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('vehicle_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('data_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('telemetryDatas')
    op.drop_table('geoDatas')
    # ### end Alembic commands ###
