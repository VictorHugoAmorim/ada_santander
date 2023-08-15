from laboratorio import Laboratorio
from medicamentos import Medicamentos
class MedicQuimio(Medicamentos):
    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, valor: float, necessita_receita: bool,) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, valor)
        self.necessita_receita = necessita_receita