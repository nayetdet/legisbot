import chromadb
from llama_index.core import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore

db = chromadb.PersistentClient(path="./chroma-db")
chroma_collection = db.get_or_create_collection("legisbot")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
