from cadastra_cliente import *
from cadastra_cliente import Cadastro
from medicamentos import *
from medic_quimio import *
from medic_fit import *
from laboratorio import *
# from vendas import *
from lendocsv import lendo_csv
import time

def sys():
    lendo_csv()
    while True:
        print('#'*30,'MENU PRINCIPAL','#'*30,'\n')
        print('1- Cadastrar cliente\n2- Alterar cadastro de cliente\n3- Consultar clientes cadastrados',sep='')
        print('4- Cadastrar medicamento\n5- Alterar cadastro de medicamento\n6- Consultar medicamentos cadastrados')
        print('7- Buscar medicamento\n0- Sair')
        user_choice = input('Por favor, escolha o número da ação desejada:\n ')
        if user_choice == '0':
            print("Encerrando o programa...")
            time.sleep(3)
            break
        elif user_choice in ['1','2','3','4','5','6','7','0']:    
            #Cadastrar clientes
            if user_choice == '1': 
                cadastro_instance = Cadastro()
                identificador, nome, data_nascimento, idade = cadastro_instance.coleta_dados()
                cadastro_instance.identificador = identificador
                cadastro_instance.nome = nome
                cadastro_instance.data_nascimento = data_nascimento
                cadastro_instance.idade = idade
                cadastros_clientes = cadastro_instance.armazena_dados()
            elif user_choice == '2': #
                try:
                    cadastro_instance.altera_cliente(cadastros_clientes)
                except:
                    print('Impossível, nenhum cadastro encontrado!\n')
            #Exibir clientes        
            elif user_choice == '3': 
                try:
                    cadastro_instance.exibe_clientes(cadastros_clientes)
                except:
                    print('Impossível, nenhum cadastro encontrado!\n')
            #Cadastrar medicamento       
            elif user_choice == '4': 
                try:
                    print('1 - Cadastrar medicamento fitoterápico\n2 - Cadastrar medicamento quimioterápico')
                    user_choice_medic = input('Por favor, escolha o número da ação desejada:\n ')
                    if user_choice_medic == '1':
                        MedicFit.cadastrar_medic_fit()
                    elif user_choice_medic =='2':
                        MedicQuimio.cadastrar_medic_quimio()
                    else:
                        print("Opção inexistente")
                except:
                    print('Erro no cadastro do medicamento!\n')
            #Listar medicamentos cadastrados
            elif user_choice == '6': 
                try:
                    print('1 - Listar todos os medicamentos cadastrados\n2 - Listar medicamentos fitoterápicos cadastrados\n3 - Listar medicamentos quimioterápicos cadastrados')
                    user_choice_listamedic = input('Por favor, escolha o número da ação desejada:\n ')
                    if user_choice_listamedic =='1':
                        print(sorted(Medicamentos.lista_medicamentos, key=lambda med:med.nome))
                    elif user_choice_listamedic =='2':
                        print(sorted(MedicFit.lista_fit, key=lambda med:med.nome))
                    elif user_choice_listamedic =='3':
                        print(sorted(MedicQuimio.lista_quimio, key=lambda med:med.nome))
                    else:
                        print("Opção inexistente")
                except:
                    print('Impossível, nenhum cadastro encontrado!\n')
            # Buscar medicamento
            elif user_choice == '7': 
                try:
                    print('1 - Buscar medicamento por nome\n2 - Buscar medicamento por laboratório\n3 - Buscar medicamento por descrição')
                    user_choice_search = input('Por favor, escolha o número da ação desejada:\n ')
                    if user_choice_search == '1':
                        termo_busca = input("Digite o nome do medicamento: ")
                        resultados = [med for med in Medicamentos.lista_medicamentos if termo_busca.lower() in med.nome.lower()]
                        if resultados:
                            print("Resultados encontrados:")
                            for med in resultados:
                                print(med)
                        else:
                            print("Nenhum resultado encontrado.")
                    elif user_choice_search == '2':
                        termo_busca = input("Digite o nome do laboratório do medicamento: ")
                        resultados = [med for med in Medicamentos.lista_medicamentos if termo_busca.lower() in med.laboratorio.nome.lower()]
                        if resultados:
                            print("Resultados encontrados:")
                            for med in resultados:
                                print(med)
                        else:
                            print("Nenhum resultado encontrado.")
                    elif user_choice_search == '3':
                        termo_busca = input("Digite a descrição do medicamento: ")
                        resultados = [med for med in Medicamentos.lista_medicamentos if termo_busca.lower() in med.descricao.lower()]
                        if resultados:
                            print("Resultados encontrados:")
                            for med in resultados:
                                print(med)
                        else:
                            print("Nenhum resultado encontrado.")
                    else:
                        print("Opção inexistente")
                except:
                    print('Impossível, nenhum cadastro encontrado!\n')        

if __name__ == '__main__':
    sys()