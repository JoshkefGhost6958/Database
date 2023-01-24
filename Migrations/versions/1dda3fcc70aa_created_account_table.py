"""Created account table

Revision ID: 1dda3fcc70aa
Revises: f5d8e3ce09a6
Create Date: 2023-01-24 10:36:25.903963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dda3fcc70aa'
down_revision = 'f5d8e3ce09a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
        create table account(acc_id int unique auto_increment
        not null,owner int not null default 1,
        accNo int unique not null,
        accBal float not null default 0.0,
        pin int not null,
        primary key(acc_id,accNo));
    """
    op.execute(sql)


def downgrade() -> None:
    op.drop_table('account')
