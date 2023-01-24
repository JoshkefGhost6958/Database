"""Created transaction table

Revision ID: 18816f0378d4
Revises: 163a4ca71897
Create Date: 2023-01-24 11:37:17.445904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18816f0378d4'
down_revision = '163a4ca71897'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
        create table transaction(
            trans_id int primary key auto_increment not null,
            account int not null,
            recipient int not null,
            amount float not null,
            conducted_time datetime default current_timestamp)
    """
    op.execute(sql)

def downgrade() -> None:
    op.drop_table('transaction')
