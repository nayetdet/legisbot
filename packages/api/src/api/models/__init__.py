from sqlalchemy.orm import DeclarativeMeta
from api.deps.postgres_instance import PostgresInstance

Base: DeclarativeMeta = PostgresInstance.get_base()
