"""Added acc_link to transaction table

Revision ID: e02f40699355
Revises: 18816f0378d4
Create Date: 2023-01-24 11:45:34.974717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e02f40699355'
down_revision = '18816f0378d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
        alter table transaction 
        add constraint acc_link 
        foreign key(account) 
        references account(acc_id);
    """
    op.execute(sql)


def downgrade() -> None:
    sql = """
        alter table transaction drop constraint acc_link;
    """
    op.execute(sql)
    #op.drop_constraint("acc_link","transaction")
