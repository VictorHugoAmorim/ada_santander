from laboratorio import Laboratorio
from medicamentos import Medicamentos
class MedicQuimio(Medicamentos):
    lista_quimio = []

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, valor: float, necessita_receita: bool,) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, valor)
        self.necessita_receita = necessita_receita
        MedicQuimio.lista_quimio.append(self)
    
    def __repr__(self) -> str:
        representacao = '\n\nNome: ' + self.nome
        representacao += '\nPrincipal composto: ' + self.principal_composto
        representacao += '\nLaboratório: ' + str(self.laboratorio.nome)
        representacao += '\nDescrição: ' + self.descricao
        representacao += '\nValor: R$' + str(self.valor)
        representacao += '\nNecessita de Receita: ' + ('sim' if self.necessita_receita else "nao")
        return representacao