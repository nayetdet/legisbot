from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers.vectorstore import AsyncDenseVectorStrategy
from llama_index.core import StorageContext
from llama_index.storage.index_store.elasticsearch import ElasticsearchIndexStore
from llama_index.storage.kvstore.elasticsearch import ElasticsearchKVStore
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from api.config import Config

class ElasticsearchInstance:
    __client: AsyncElasticsearch = AsyncElasticsearch(hosts=[Config.ELASTICSEARCH_HOST_URL])
    __vector_store: ElasticsearchStore = ElasticsearchStore(es_client=__client, index_name="vectors", retrieval_strategy=AsyncDenseVectorStrategy())
    __index_store: ElasticsearchIndexStore = ElasticsearchIndexStore(ElasticsearchKVStore(es_client=__client, index_name="indexes"))

    @classmethod
    def get_storage_context(cls) -> StorageContext:
        return StorageContext.from_defaults(
            index_store=cls.__index_store,
            vector_store=cls.__vector_store
        )
