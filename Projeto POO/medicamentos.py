from laboratorio import Laboratorio

class Medicamentos:
    lista_medicamentos = []

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, valor: float) -> None:
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.valor = valor
        Medicamentos.lista_medicamentos.append(self)
    
    def __repr__(self) -> str:
        representacao = '\n\nNome: ' + self.nome
        representacao += '\nPrincipal composto: ' + self.principal_composto
        representacao += '\nLaboratório: ' + str(self.laboratorio.nome)
        representacao += '\nDescrição: ' + self.descricao
        representacao += '\nValor: R$' + str(self.valor)
        return representacao