from medicamentos import Medicamentos
from medic_fit import MedicFit
from medic_quimio import MedicQuimio

class Relatorio:
    def __init__(self) -> None:
       pass 
    
    def listar_clientes(self) -> str:
        pass

    def listar_medicamentos(self) -> str:
        return Medicamentos.lista_medicamentos.sort

    def listar_quimios(self) -> str:
        return MedicQuimio.lista_quimio.sort

    def listar_fito(self) -> str:
        return MedicFit.lista_fit.sort

