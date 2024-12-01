from llama_index.core import GPTVectorStoreIndex, Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from QAwithdocs.data_ingestion import load_data
from QAwithdocs.model_api import load_model
import sys
from exception import customexception
from logger import logging


def download_gemini_embedding(model, documents):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Args:
        model: The LLM to be used in the embedding process.
        documents: List of documents to process and index.

    Returns:
        query_engine: A query engine for running similarity queries on the indexed documents.
    """
    try:
        logging.info("Initializing Gemini embedding model and settings...")
        
       
        Settings.llm = model
        Settings.embed_model = GeminiEmbedding(model_name="models/embedding-001")
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20
        
        logging.info("Creating the vector store index from documents...")
        
       
        index = GPTVectorStoreIndex.from_documents(
            documents,
            embed_model=Settings.embed_model,
            llm=Settings.llm,
            chunk_size=Settings.chunk_size,
            chunk_overlap=Settings.chunk_overlap
        )
        
     
        logging.info("Persisting the index storage context...")
        index.storage_context.persist()

      
        logging.info("Creating the query engine...")
        query_engine = index.as_query_engine()

        logging.info("Query engine created successfully.")
        return query_engine
    except Exception as e:
        logging.error(f"Error occurred while downloading and processing Gemini embedding: {e}")
        raise customexception(e, sys)
