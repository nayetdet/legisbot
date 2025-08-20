from typing import Sequence
from llama_index.core import VectorStoreIndex
from llama_index.core.schema import BaseNode
from api.deps.databases.chroma_instance import ChromaInstance
from api.deps.llms.ollama_instance import OllamaInstance

class DocumentRepository:
    @staticmethod
    def create(nodes: Sequence[BaseNode]) -> None:
        index: VectorStoreIndex = VectorStoreIndex(
            nodes,
            embed_model=OllamaInstance.get_embedding(),
            storage_context=ChromaInstance.get_storage_context()
        )

        index.storage_context.persist()

    @staticmethod
    def delete_by_filename(filename: str) -> None:
        ChromaInstance.get_collection().delete(where={
            "filename": filename
        })

        ChromaInstance.get_storage_context().persist()
