from laboratorio import Laboratorio
from medicamentos import Medicamentos
class MedicQuimio(Medicamentos):
    lista_quimio = []

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, valor: float, necessita_receita: bool,) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, valor)
        self.necessita_receita = necessita_receita
        MedicQuimio.lista_quimio.append(self)
    
    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nPrincipal composto: ' + self.principal_composto
        representacao += '\nLaboratório: ' + self.laboratorio
        representacao += '\nDescrição: ' + self.descricao
        representacao += '\nValor: R$' + self.valor
        representacao += '\nNecessita de Receita: ' + self.necessita_receita
        return representacao