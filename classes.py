from typing import List


class Cuidador:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento


class Habilidade:
    def __init__(self, nome: str, descricao: str = ''):
        self.nome = nome
        self.descricao = descricao

class Personagem:
    def __init__(self, nome: str, classe: str, nivel: int, habilidades: List[Habilidade]):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.habilidades = habilidades
