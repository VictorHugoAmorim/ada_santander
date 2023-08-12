from laboratorio import Laboratorio

class MedicQuimio:
    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, necessita_receita: bool) -> None:
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.necessita_receita = necessita_receita