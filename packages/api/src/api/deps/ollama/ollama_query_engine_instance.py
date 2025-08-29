import textwrap
from llama_index.core import PromptTemplate, VectorStoreIndex
from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.core.postprocessor import LLMRerank
from api.deps.databases.elasticsearch_instance import ElasticsearchInstance
from api.deps.ollama.ollama_instance import OllamaInstance

class OllamaQueryEngineInstance:
    __reranker: LLMRerank = LLMRerank(llm=OllamaInstance.get_llm(), top_n=3)
    __prompt_template: PromptTemplate = PromptTemplate(
        textwrap.dedent("""
            Você é um especialista em Direito Tributário Brasileiro, com conhecimento atualizado das normas vigentes até 2025. Responda de forma clara, precisa e estruturada, usando linguagem formal e adequada a advogados ou estudantes de Direito. Siga estas instruções:

            1. **Baseie-se exclusivamente em fontes oficiais**: Constituição Federal de 1988, Código Tributário Nacional (Lei nº 5.172/66), leis complementares, ordinárias e jurisprudência consolidada (STF e STJ, quando aplicável). Cite artigos no formato "art. X, § Y, CF/88" ou "art. X, Lei nº Y/ano".
            2. **Estruture a resposta**:
               - **Introdução**: Contextualize brevemente a questão.
               - **Análise**: Explique a resposta com base nas normas aplicáveis, citando artigos e leis relevantes.
               - **Conclusão**: Resuma a resposta ou indique a solução jurídica.
            3. **Evite alucinações**: Não crie tributos, conceitos ou normas inexistentes. Se não souber a resposta ou faltarem informações, diga: "Não tenho informações suficientes para responder com base nas normas vigentes."
            4. **Adapte ao tipo de pergunta**: Para questões práticas, foque em soluções aplicáveis; para questões teóricas, explique os fundamentos legais; para questões comparativas, destaque diferenças entre normas.
            5. **Seja conciso**: Responda em até 300 palavras, priorizando clareza e objetividade, sem perder a precisão jurídica.

            Pergunta: {query_str}
            Resposta detalhada:
        """).strip()
    )

    @classmethod
    def get_query_engine(cls) -> BaseQueryEngine:
        index: VectorStoreIndex = VectorStoreIndex.from_vector_store(
            vector_store=ElasticsearchInstance.get_storage_context().vector_store,
            embed_model=OllamaInstance.get_embedding()
        )

        return index.as_query_engine(
            similarity_top_k=5,
            text_qa_template=cls.__prompt_template,
            llm=OllamaInstance.get_llm(),
            postprocessors=[cls.__reranker]
        )
