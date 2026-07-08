import pickle
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# CLASSE ABSTRATA DAO 
# ---------------------------------------------------------
class DAO(ABC):
    def __init__(self, datasource: str):
        self.__datasource = datasource
        self.__cache = {}  # Usando dicionário {cpf: objeto} para facilitar o get(key)
        self.__load()

    def __dump(self):
        """Grava os dados do cache para o arquivo binário (Serialização)."""
        with open(self.__datasource, 'wb') as f:
            pickle.dump(self.__cache, f)

    def __load(self):
        """Lê os dados do arquivo binário para o cache (Desserialização)."""
        try:
            with open(self.__datasource, 'rb') as f:
                self.__cache = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.__cache = {}

    def add(self, key, obj):
        """Adiciona um objeto ao cache e atualiza o arquivo."""
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        """Busca um objeto no cache pela chave."""
        return self.__cache.get(key, None)

    def remove(self, key):
        """Remove um objeto do cache e atualiza o arquivo."""
        if key in self.__cache:
            del self.__cache[key]
            self.__dump()

    def get_all(self) -> list:
        """Retorna todos os objetos salvos no cache."""
        return list(self.__cache.values())