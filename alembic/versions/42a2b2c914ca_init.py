"""init

Revision ID: 42a2b2c914ca
Revises:
Create Date: 2023-12-16 04:25:11.086437

"""
from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "42a2b2c914ca"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("comments")
    op.drop_table("histories")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_index("ix_users_username", table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("username", sa.VARCHAR(), nullable=True),
        sa.Column("hashed_password", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_users_username", "users", ["username"], unique=False)
    op.create_index("ix_users_id", "users", ["id"], unique=False)
    op.create_table(
        "histories",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("page", sa.VARCHAR(length=100), nullable=False),
        sa.Column("timestamp", sa.DATETIME(), nullable=True),
        sa.Column("user_id", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "comments",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("content", sa.VARCHAR(), nullable=False),
        sa.Column("timestamp", sa.DATETIME(), nullable=True),
        sa.Column("user_id", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###