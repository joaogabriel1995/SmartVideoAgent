# src/infrastructure/qdrant_storage.py
from infrastructure.qdrant.vector_storage_interface import VectorStorageInterface
from qdrant_client import QdrantClient

class QdrantStorage(VectorStorageInterface):

    def __init__(self, host="localhost", port=6333):
        self.client = QdrantClient(host, port)
        

    def create_collection(self):
        pass


    def store(self, embeddings, metadata):
        # Lógica para armazenar no Qdrant
        pass