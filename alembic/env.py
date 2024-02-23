# alembic/env.py
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# ...

def run_migrations_offline():
    # ...

def run_migrations_online():
    # ...

# ...

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
