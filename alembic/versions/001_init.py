"""init
Revision ID: 001
Revises: 
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('patients',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('oms_policy', sa.String(16), unique=True),
        sa.Column('birth_date', sa.Date()),
        sa.Column('email', sa.String()),
        sa.Column('gender', sa.String())
    )
    op.create_index('ix_name', 'patients', ['full_name'])

def downgrade(): op.drop_table('patients')