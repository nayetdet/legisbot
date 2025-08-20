from typing import Generator
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, DeclarativeMeta
from api.config import Config

class PostgresInstance:
    __engine: Engine = create_engine(Config.POSTGRES_HOST_URL)
    __session_local: sessionmaker[Session] = sessionmaker(bind=__engine, autocommit=False, autoflush=False)
    __base: DeclarativeMeta = declarative_base()

    @classmethod
    def get_base(cls) -> DeclarativeMeta:
        return cls.__base

    @classmethod
    def get_db(cls) -> Generator[Session, None, None]:
        db: Session = cls.__session_local()
        try: yield db
        finally:
            db.close()
