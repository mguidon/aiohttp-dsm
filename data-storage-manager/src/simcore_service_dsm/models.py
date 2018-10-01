import sqlalchemy as sa

metadata = sa.MetaData()

# User
users = sa.Table(
    "users", metadata,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("login", sa.String(256), nullable=False),
    sa.Column("passwd", sa.String(256), nullable=False),
    sa.Column("is_superuser", sa.Boolean, nullable=False,
              server_default="FALSE"),
    sa.Column("disabled", sa.Boolean, nullable=False,
              server_default="FALSE"),

    # indices
    sa.PrimaryKeyConstraint("id", name="user_pkey"),
    sa.UniqueConstraint("login", name="user_login_key"),
)
