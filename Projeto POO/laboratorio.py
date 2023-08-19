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
    
    def verifica_laboratorio(self, nome: str):
        laboratorio_associado = next((lab for lab in Laboratorio.lista_laboratorios if lab.nome == nome), None)

        if laboratorio_associado is None:
            print("Laboratório ainda não cadastrado! Portanto informe:")
            endereco = input("Endereço do laboratório: ")
            telefone = input("Telefone do laboratório: ")
            cidade = input("Cidade do laboratório: ")
            estado = input("Estado do laboratório: ")

            laboratorio_associado = Laboratorio(
                nome=nome,
                endereco=endereco,
                telefone=telefone,
                cidade=cidade,
                estado=estado
            )
        return laboratorio_associado
