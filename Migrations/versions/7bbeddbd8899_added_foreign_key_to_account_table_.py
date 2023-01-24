"""added foreign key to account table refrencing user table

Revision ID: 7bbeddbd8899
Revises: 1dda3fcc70aa
Create Date: 2023-01-24 10:54:45.920163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bbeddbd8899'
down_revision = '1dda3fcc70aa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
    ALTER TABLE account ADD CONSTRAINT user_fk FOREIGN KEY(owner)
    REFERENCES user(id);"""
    op.execute(sql)


def downgrade() -> None:
    sql = """
        ALTER TABLE account DROP CONSTRAINT user_fk;
    """
    #op.drop_constraint(constraint_name="user_fk",table_name="user",type="foreignkey")
    op.execute(sql)