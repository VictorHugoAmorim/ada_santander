class Laboratorio:
    lista_laboratorios = []

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        Laboratorio.lista_laboratorios.append(self)
    
    def __repr__(self) -> str:
        representacao = '\nNome: ' + self.nome
        representacao += '\nEndereço: ' + self.endereco
        representacao += '\nTelefone: ' + self.telefone
        representacao += '\nCidade: ' + self.cidade
        representacao += '\nEstado: R$' + self.estado + '\n'
        return representacao
