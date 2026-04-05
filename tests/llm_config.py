# tests/llm_config.py
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_ollama import ChatOllama, OllamaEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

def get_langchain_llm():
    if LLM_PROVIDER == "openai":
        return ChatOpenAI(model=OPENAI_MODEL, temperature=0)
    return ChatOllama(model=OLLAMA_MODEL, temperature=0,base_url="http://localhost:11434",)

def get_langchain_embeddings():
    if LLM_PROVIDER == "openai":
        return OpenAIEmbeddings(model=OPENAI_EMBED_MODEL)
    return OllamaEmbeddings(model=OLLAMA_EMBED_MODEL,base_url="http://localhost:11434", )

def get_ragas_llm():
    return LangchainLLMWrapper(get_langchain_llm())

def get_ragas_embeddings():
    return LangchainEmbeddingsWrapper(get_langchain_embeddings())