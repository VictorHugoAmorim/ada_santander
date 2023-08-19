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
    
    def cadastrar_medic_quimio(self) -> str:
        nome = input("Nome do medicamento: ")
        principal_composto = input("Principal composto: ")
        laboratorio = input("Laboratório: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor de venda: "))
        receita = input("Necessita de receita? ")

        if (receita.lower != 's' or 'sim' or 'yes' or 'y' or 'n' or 'nao' or 'não' or 'no' or True or False):
            print("Resposta inválida. Digite 'sim' ou 'nao'.")
            receita = input("Necessita de receita? ")

        if (receita.lower == 's' or 'sim' or 'yes' or 'y'):
            receita = True
        elif (receita.lower == 'n' or 'nao' or 'não' or 'no'):
            receita = False
            
        laboratorio_associado = Laboratorio.verifica_laboratorio(laboratorio)

        novo_medicamento = MedicQuimio(
            nome=nome,
            principal_composto=principal_composto,
            laboratorio=laboratorio_associado,
            descricao=descricao,
            valor=valor,
            necessita_receita=receita
        )

        print("Medicamento quimioterápico cadastrado com sucesso!")
