from laboratorio import Laboratorio

class Medicamentos:
    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, valor: float) -> None:
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.valor = valor