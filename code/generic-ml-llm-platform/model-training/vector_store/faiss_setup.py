from typing import List
import faiss
import numpy as np

class FAISSSearch:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)  # Using L2 distance for similarity search

    def add_vectors(self, vectors: List[np.ndarray]):
        """Add vectors to the FAISS index."""
        self.index.add(np.array(vectors).astype('float32'))

    def search(self, query_vector: np.ndarray, k: int = 5):
        """Search for the k nearest neighbors of the query vector."""
        distances, indices = self.index.search(query_vector.reshape(1, -1).astype('float32'), k)
        return distances, indices

    def save_index(self, file_path: str):
        """Save the FAISS index to a file."""
        faiss.write_index(self.index, file_path)

    def load_index(self, file_path: str):
        """Load the FAISS index from a file."""
        self.index = faiss.read_index(file_path)