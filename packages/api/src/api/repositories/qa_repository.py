from typing import Optional
from api.deps.databases.postgres_instance import PostgresInstance
from api.models.qa import QA

class QARepository:
    @staticmethod
    def get_by_id(qa_id: int) -> Optional[QA]:
        with PostgresInstance().get_db() as session:
            return session.get(QA, qa_id)

    @staticmethod
    def create(qa: QA) -> QA:
        with PostgresInstance.get_db() as session:
            session.add(qa)
            session.commit()
            session.refresh(qa)
        return qa

    @staticmethod
    def delete_by_id(qa_id: int) -> None:
        with PostgresInstance.get_db() as session:
            qa: Optional[QA] = session.get(QA, qa_id)
            if qa is None:
                return

            session.delete(qa)
            session.commit()
            session.refresh(qa)
