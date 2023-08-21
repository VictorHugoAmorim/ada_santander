import csv
from laboratorio import *
from medic_fit import *
from medic_quimio import *

PATH1 = '.\csv'
PATH2 = 'Projeto POO/csv/'

def lendo_csv():
    try:
        with open(rf'{PATH1}\labs.csv', 'r', encoding='utf-8') as arquivo_labs_csv:

            labs_csv = csv.DictReader(arquivo_labs_csv)
            for linha in labs_csv:
              linha['nome'] = Laboratorio(
              linha['nome'],
              linha['endereco'],
              linha['telefone'],
              linha['cidade'],
              linha['estado']
            )
    except:
        with open(rf'{PATH2}\labs.csv', 'r', encoding='utf-8') as arquivo_labs_csv:

            labs_csv = csv.DictReader(arquivo_labs_csv)
            for linha in labs_csv:
              linha['nome'] = Laboratorio(
              linha['nome'],
              linha['endereco'],
              linha['telefone'],
              linha['cidade'],
              linha['estado']
            )

    
    try:
        with open(rf'{PATH1}\fito.csv', 'r', encoding='utf-8') as arquivo_fito_csv:
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
    except:
        with open(rf'{PATH2}\fito.csv', 'r', encoding='utf-8') as arquivo_fito_csv:
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
    try:
        with open(rf'{PATH1}\quimio.csv', 'r', encoding='utf-8') as arquivo_quimio_csv:
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
    except:
        with open(rf'{PATH2}\quimio.csv', 'r', encoding='utf-8') as arquivo_quimio_csv:
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

# Teste ----------------------------------------------------------

TESTE = 0 # Para testar deixar True:
if (TESTE):
    print('\n\n VOCE ESTA RODANDO UM TESTE \n\n')
    lendo_csv()
    print("Objetos instanciados...")
    print(Laboratorio.lista_laboratorios)
    print(MedicFit.lista_fit)
    print(MedicQuimio.lista_quimio)    
