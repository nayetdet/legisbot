from typing import Sequence, List
from fastapi import UploadFile
from tempfile import NamedTemporaryFile
from llama_index.core import Document
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.readers.file.base import SimpleDirectoryReader
from api.deps.databases.elasticsearch_instance import ElasticsearchInstance
from api.deps.ollama.ollama_instance import OllamaInstance

class IngestService:
    @staticmethod
    def ingest(file: UploadFile, filename: str) -> None:
        file.file.seek(0)
        with NamedTemporaryFile(suffix=filename) as tmp:
            tmp.write(file.file.read())
            tmp.flush()

            reader: SimpleDirectoryReader = SimpleDirectoryReader(input_files=[tmp.name])
            documents: List[Document] = reader.load_data(show_progress=True)
            for document in documents:
                document.extra_info = document.extra_info or {}
                document.extra_info["filename"] = filename

        pipeline: IngestionPipeline = IngestionPipeline(
            transformations=[
                SentenceSplitter(chunk_size=512, chunk_overlap=64),
                OllamaInstance.get_embedding()
            ],
            vector_store=ElasticsearchInstance.get_storage_context().vector_store
        )

        pipeline.run(documents=documents, num_workers=4, in_place=True, show_progress=True)
