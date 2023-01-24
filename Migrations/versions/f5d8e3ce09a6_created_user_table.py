"""Created user table

Revision ID: f5d8e3ce09a6
Revises: 
Create Date: 2023-01-24 10:13:10.783653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5d8e3ce09a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
        create table user(
            id int primary key unique auto_increment not null,
            username varchar(25) not null,
            fname varchar(15) not null,
            lname varchar(15) not null,
            national_id int not null,
            account int not null);
    """
    op.execute(sql)


def downgrade() -> None:
    op.drop_table("user")

