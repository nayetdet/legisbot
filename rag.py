from llama_index.core.postprocessor import LLMRerank
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, PromptTemplate
from database import storage_context
from embedding import embedding

llm = Ollama(model="llama3.2:1b", request_timeout=6000)
index = VectorStoreIndex.from_vector_store(storage_context.vector_store, embed_model=embedding)

template_str = """
<wait>
1. Analise profundamente a pergunta tributária em relação ao contexto jurídico
2. Revise mentalmente os artigos do CTN e legislação pertinente
3. Verifique possíveis interpretações doutrinárias relevantes
4. Considere jurisprudência do CARF e STJ sobre o tema
5. Confira a coerência lógica da resposta antes de formular
</wait>

Você é um especialista em direito tributário brasileiro. Responda STRICTO SENSU ao solicitado, **exclusivamente em português**.

# Formato de Resposta:
- Fundamento Legal: (cite dispositivos legais com precisão)
- Análise Técnica: (3 etapas de raciocínio jurídico)
- Confirmação: (validação cruzada com doutrina)

# Regras Aprimoradas:
- Linguagem técnica com precisão terminológica
- Citação completa de artigos/parágrafos do CTN
- Máximo 200 palavras
- Hierarquia normativa explícita
- Se não houver informações suficientes no contexto, diga explicitamente: "Não encontrei base suficiente para responder com precisão". Não invente ou deduza além do fornecido.

Contexto fornecido: {context_str}

<answer>
Pergunta: {query_str}
Resposta:
""".strip()

qa_template = PromptTemplate(template_str)
reranker = LLMRerank(llm=llm, top_n=5)
retriever = index.as_retriever(similarity_top_k=5)
retriever.postprocessors = [reranker]
query_engine = RetrieverQueryEngine.from_args(retriever=retriever,llm=llm,streaming=True)
