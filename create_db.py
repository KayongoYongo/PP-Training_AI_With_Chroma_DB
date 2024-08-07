import chromadb
from typing import List
from create_embedding import GeminiEmbeddingFunction

def create_chroma_db(documents:List, path:str, name:str):
    """
    Creates a Chroma database using the provided documents, path, and collection name.

    Parameters:
    - documents: An iterable of documents to be added to the Chroma database.
    - path (str): The path where the Chroma database will be stored.
    - name (str): The name of the collection within the Chroma database.

    Returns:
    - Tuple[chromadb.Collection, str]: A tuple containing the created Chroma Collection and its name.
    """

    chroma_client = chromadb.PersistentClient(path=path)

    db = chroma_client.create_collection(name=name,
                                         embedding_function=GeminiEmbeddingFunction())
    
    for i, doc in enumerate(documents):
        db.add(documents=doc, ids=str(i))

    return db, name