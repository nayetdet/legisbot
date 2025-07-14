from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.extractors import TitleExtractor, QuestionsAnsweredExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from database import storage_context

def main():
    docs = SimpleDirectoryReader(input_dir="./data", recursive=True).load_data()
    for doc in docs:
        doc.text_template = "Metadata:\n{metadata_str}\n---\nContent:\n{content}"
        for metadata in ["filename", "page_label"]:
            if metadata not in doc.excluded_embed_metadata_keys:
                doc.excluded_embed_metadata_keys.append(metadata)

    llm = Ollama(model="qwen:0.5b", request_timeout=6000)
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(separator=" ", chunk_size=1024, chunk_overlap=128),
            TitleExtractor(llm=llm, nodes=5),
            QuestionsAnsweredExtractor(llm=llm, questions=3)
        ]
    )

    nodes = pipeline.run(documents=docs, in_place=True, show_progress=True)
    hf_embeddings = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    index = VectorStoreIndex(nodes, embed_model=hf_embeddings, storage_context=storage_context)
    index.storage_context.persist(persist_dir="./storage")

if __name__ == "__main__":
    main()
