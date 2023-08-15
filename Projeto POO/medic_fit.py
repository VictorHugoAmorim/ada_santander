from laboratorio import Laboratorio
from medicamentos import Medicamentos
class MedicFit(Medicamentos):
    lista_fit = []

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, valor: float) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, valor)
        MedicFit.lista_fit.append(self)
