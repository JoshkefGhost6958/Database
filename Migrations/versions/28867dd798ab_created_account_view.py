"""created Account view

Revision ID: 28867dd798ab
Revises: e02f40699355
Create Date: 2023-01-24 12:20:10.057648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28867dd798ab'
down_revision = 'e02f40699355'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
        create view user_account as 
        select accNo,accBal,
        transaction.amount,
        count(account) as transactions,
        (accBal-amount) as balance from account 
        inner join transaction 
        on account.acc_id = transaction.account;
    """
    op.execute(sql)


def downgrade() -> None:
    sql = "drop view user_account;"
    op.execute(sql)
