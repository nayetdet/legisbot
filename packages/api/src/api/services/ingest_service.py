from typing import Sequence
from fastapi import UploadFile
from llama_index.core import Document
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import BaseNode
from api.repositories.document_repository import DocumentRepository

class IngestService:
    @staticmethod
    def ingest(file: UploadFile, filename: str) -> None:
        document: Document = Document(
            text=file.file.read(),
            extra_info={
                "filename": filename
            }
        )

        pipeline: IngestionPipeline = IngestionPipeline(
            transformations=[
                SentenceSplitter(chunk_size=1024, chunk_overlap=128)
            ]
        )

        nodes: Sequence[BaseNode] = pipeline.run(documents=[document], in_place=True, show_progress=True)
        DocumentRepository.create(nodes)

    @staticmethod
    def delete_by_filename(filename: str) -> None:
        DocumentRepository.delete_by_filename(filename)
