from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from database import storage_context
from embedding import embedding

def main():
    docs = SimpleDirectoryReader(input_dir="./data", recursive=True).load_data()
    for doc in docs:
        doc.text_template = "Metadata:\n{metadata_str}\n---\nContent:\n{content}"
        for metadata in ["filename", "page_label"]:
            if metadata not in doc.excluded_embed_metadata_keys:
                doc.excluded_embed_metadata_keys.append(metadata)

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=1024, chunk_overlap=128)
        ]
    )

    nodes = pipeline.run(documents=docs, in_place=True, show_progress=True)
    index = VectorStoreIndex(nodes, embed_model=embedding, storage_context=storage_context)
    index.storage_context.persist(persist_dir="./storage")

if __name__ == "__main__":
    main()
