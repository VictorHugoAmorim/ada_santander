from laboratorio import Laboratorio
from medicamentos import Medicamentos
class MedicFit(Medicamentos):
    lista_fit = []

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, valor: float) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, valor)
        MedicFit.lista_fit.append(self)
    
    @staticmethod
    def cadastrar_medic_fit():
        nome = input("Nome do medicamento: ")
        principal_composto = input("Principal composto: ")
        laboratorio = input("Laboratório: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor de venda: "))

        laboratorio_associado = Laboratorio.verifica_laboratorio(laboratorio)

        novo_medicamento = MedicFit(
            nome=nome,
            principal_composto=principal_composto,
            laboratorio=laboratorio_associado,
            descricao=descricao,
            valor=valor,
        )
        
        print("Medicamento fitoterápico cadastrado com sucesso!")
