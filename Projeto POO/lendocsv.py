import csv
from laboratorio import *
from medic_fit import *
from medic_quimio import *

def lendo_csv():

    with open(r'.\csv\labs.csv', 'r', encoding='utf-8') as arquivo_labs_csv:
        labs_csv = csv.DictReader(arquivo_labs_csv)
        for linha in labs_csv:
          linha['nome'] = Laboratorio(
          linha['nome'],
          linha['endereco'],
          linha['telefone'],
          linha['cidade'],
          linha['estado']
        )
    
    with open(r'.\csv\fito.csv', 'r', encoding='utf-8') as arquivo_fito_csv:
        fito_csv = csv.DictReader(arquivo_fito_csv)
    
        for linha in fito_csv:
            laboratorio_associado = next((lab for lab in Laboratorio.lista_laboratorios if lab.nome == linha['laboratorio']), None)
            linha['nome'] = MedicFit(
                nome=linha['nome'],
                principal_composto=linha['principal_composto'],
                laboratorio=laboratorio_associado,
                descricao=linha['descricao'],
                valor=float(linha['valor'])
            )
    
    with open(r'.\csv\quimio.csv', 'r', encoding='utf-8') as arquivo_quimio_csv:
        quimio_csv = csv.DictReader(arquivo_quimio_csv)
    
        for linha in quimio_csv:
            laboratorio_associado = next((lab for lab in Laboratorio.lista_laboratorios if lab.nome == linha['laboratorio']), None)
            linha['nome'] = MedicQuimio(
                nome=linha['nome'],
                principal_composto=linha['principal_composto'],
                laboratorio=laboratorio_associado,
                descricao=linha['descricao'],
                necessita_receita=bool(linha['necessita_receita']),
                valor=float(linha['valor'])
            )
#Para testar, descomentar as linhas abaixo:
# lendo_csv()
# print("Objetos instanciados...")
# print(Laboratorio.lista_laboratorios)
# print(MedicFit.lista_fit)
# print(MedicQuimio.lista_quimio)      
