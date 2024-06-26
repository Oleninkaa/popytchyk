"""Table creation

Revision ID: df0b32bccee0
Revises: 
Create Date: 2024-04-10 23:18:05.577944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df0b32bccee0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
                    op.create_table('trips',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.Column('surname', sa.String(length=50), nullable=False),
                    sa.Column('phone', sa.String(length=15), nullable=False),
                    sa.Column('email', sa.String(length=100), nullable=False),
                    sa.Column('start', sa.String(), nullable=False),
                    sa.Column('finish', sa.String(), nullable=False),
                    sa.Column('date', sa.String(), nullable=False),
                    sa.Column('comment', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trips')
    # ### end Alembic commands ###
