from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, PromptTemplate
from database import storage_context

llm = Ollama(model="deepseek-r1:1.5b", request_timeout=6000)
hf_embeddings = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
index = VectorStoreIndex.from_vector_store(storage_context.vector_store, embed_model=hf_embeddings)

template_str = """
<wait>
1. Analise profundamente a pergunta tributária em relação ao contexto jurídico
2. Revise mentalmente os artigos do CTN e legislação pertinente
3. Verifique possíveis interpretações doutrinárias relevantes
4. Considere jurisprudência do CARF e STJ sobre o tema
5. Confira a coerência lógica da resposta antes de formular
</wait>

Você é um especialista em direito tributário brasileiro. Responda STRICTO SENSU ao solicitado:

# Formato de Resposta:
- Fundamento Legal: (cite dispositivos legais com precisão)
- Análise Técnica: (3 etapas de raciocínio jurídico)
- Confirmação: (validação cruzada com doutrina)

# Regras Aprimoradas:
- Linguagem técnica com precisão terminológica
- Citação completa de artigos/parágrafos do CTN
- Máximo 200 palavras
- Hierarquia normativa explícita
- Se não houver informações suficientes no contexto, diga explicitamente: "Não encontrei base suficiente para responder com precisão" Não invente ou deduza além do fornecido.

Contexto fornecido: {context_str}

<answer>
Pergunta: {query_str}
Resposta:
""".strip()

qa_template = PromptTemplate(template_str)
query_engine = index.as_query_engine(llm=llm, similarity_top_k=5, streaming=True)
query_engine.update_prompts({"response_synthesizer:text_qa_template": qa_template})
