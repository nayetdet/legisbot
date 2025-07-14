from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex,PromptTemplate
from database import storage_context

llm = Ollama(model="deepseek-r1:1.5b", request_timeout=6000)
hf_embeddings = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
index = VectorStoreIndex.from_vector_store(storage_context.vector_store, embed_model=hf_embeddings)
query_engine = index.as_query_engine(llm=llm, similarity_top_k=4, streaming=True)

template_str = (
    "Você é um advogado tributarista especializado em legislação brasileira.\n"
    "SIGA ESTAS REGRAS ESTRITAMENTE:\n"
    "1. Responda SOMENTE em português brasileiro\n"
    "2. Seja conciso (máximo 200 palavras)\n"
    "3. Fundamente respostas APENAS no contexto fornecido\n"
    "4. Formate com clareza (itens, parágrafos curtos)\n"
    "5. Se não houver informação suficiente, diga: 'Não há dados suficientes no contexto fornecido'\n"
    "\n"
    "Contexto:\n"
    "-------------\n"
    "{context_str}\n"
    "-------------\n"
    "\n"
    "Pergunta: {query_str}\n"
    "\n"
    "Resposta (objetiva e técnica):"
)

qa_template = PromptTemplate(template_str)
query_engine.update_prompts({"response_synthesizer:text_qa_template": qa_template})
