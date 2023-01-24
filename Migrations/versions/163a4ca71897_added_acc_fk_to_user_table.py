"""Added acc_fk to user table

Revision ID: 163a4ca71897
Revises: 7bbeddbd8899
Create Date: 2023-01-24 11:24:51.045354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '163a4ca71897'
down_revision = '7bbeddbd8899'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
        alter table user add constraint acc_fk 
        foreign key(account) 
        references account(acc_id);
    """
    op.execute(sql)

def downgrade() -> None:
    sql = """
         alter table user drop foreign key acc_fk;
    """
    #op.drop_constraint(constraint_name="acc_fk",table_name="account",type_="foreignkey")
    op.execute(sql)