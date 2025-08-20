import textwrap
from llama_index.core import PromptTemplate, VectorStoreIndex
from llama_index.core.base.base_retriever import BaseRetriever
from llama_index.core.postprocessor import LLMRerank
from llama_index.core.query_engine import RetrieverQueryEngine
from api.deps.databases.chroma_instance import ChromaInstance
from api.deps.llms.ollama_instance import OllamaInstance

class OllamaQueryEngineInstance:
    __index: VectorStoreIndex = VectorStoreIndex.from_vector_store(ChromaInstance.get_vector_store(), embed_model=OllamaInstance.get_embedding())
    __retriever: BaseRetriever = __index.as_retriever()

    __reranker: LLMRerank = LLMRerank(llm=OllamaInstance.get_llm(), top_n=5)
    __prompt_template: PromptTemplate = PromptTemplate(
        textwrap.dedent("""
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
            - Se não houver informações suficientes no contexto, diga explicitamente: 
              "Não encontrei base suficiente para responder com precisão". Não invente ou deduza além do fornecido.

            Contexto fornecido: {context_str}

            <answer>
            Pergunta: {query_str}
            Resposta:
        """).strip()
    )

    __query_engine: RetrieverQueryEngine = RetrieverQueryEngine.from_args(
        retriever=__retriever,
        llm=OllamaInstance.get_llm(),
        text_qa_template=__prompt_template,
        node_postprocessors=[__reranker]
    )

    @classmethod
    def get_query_engine(cls):
        return cls.__query_engine
