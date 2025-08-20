import chromadb
from chromadb.api.client import Client
from chromadb.config import Settings
from llama_index.core import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from api.config import Config

class ChromaInstance:
    __client: Client = chromadb.Client(Settings(chroma_api_impl="rest", chroma_server_host=Config.CHROMA_HOST_URL))
    __collection: chromadb.Collection = __client.get_collection(Config.CHROMA_COLLECTION_NAME)
    __vector_store: ChromaVectorStore = ChromaVectorStore(chroma_collection=__collection)
    __storage_context: StorageContext = StorageContext.from_defaults(vector_store=__vector_store)

    @classmethod
    def get_chroma(cls) -> Client:
        return cls.__client

    @classmethod
    def get_collection(cls) -> chromadb.Collection:
        return cls.__collection

    @classmethod
    def get_vector_store(cls) -> ChromaVectorStore:
        return cls.__vector_store

    @classmethod
    def get_storage_context(cls) -> StorageContext:
        return cls.__storage_context
