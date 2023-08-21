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
        print('1- Clientes (Cadastrar / Alterar)\n2- Medicamentos (Cadastrar / Alterar / Buscar)\n3- Iniciar venda',sep='')
        print('4- Emitir relatórios (Listar clientes / Listar medicamentos / Estatísticas )\n0- Sair')
        user_choice = input('Por favor, escolha o número da ação desejada:\n ')
        if user_choice == '0':
            print("Encerrando o programa...")
            time.sleep(3)
            break
        elif user_choice in ['1','2','3','4','0']:    
            if user_choice == '1': # Clientes
                print('1 - Cadastrar cliente\n2 - Alterar cadastro de cliente')
                user_choice_cliente = input('Por favor, escolha o número da ação desejada:\n ')
                if user_choice_cliente == '1':  # Cadastrar clientes
                    cadastro_instance = Cadastro()
                    identificador, nome, data_nascimento, idade = cadastro_instance.coleta_dados()
                    cadastro_instance.identificador = identificador
                    cadastro_instance.nome = nome
                    cadastro_instance.data_nascimento = data_nascimento
                    cadastro_instance.idade = idade
                    cadastros_clientes = cadastro_instance.armazena_dados()
                elif user_choice_cliente == '2': # Alterar cadastro de clientes
                    try:
                        cadastro_instance.altera_cliente(cadastros_clientes)
                    except:
                        print('Impossível, nenhum cadastro encontrado!\n')
                else:
                    print("Opção inexistente")
         
            #Medicamentos       
            elif user_choice == '2': 
                    print('1 - Cadastrar medicamento\n2 - Alterar medicamento\n3 - Buscar medicamento')
                    user_choice_medicamento = input('Por favor, escolha o número da ação desejada:\n ')
                    if user_choice_medicamento == '1': #Cadastrar medicamento
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

                    elif user_choice_medicamento == '2': #Alterar medicamento
                        nome_medicamento = input('Digite o nome do medicamento que deseja alterar:\n')
                        medicamento_alterar = None
        
                        while not medicamento_alterar:
                            for med in Medicamentos.lista_medicamentos:
                                if med.nome.lower() == nome_medicamento.lower():
                                    medicamento_alterar = med
                                    break
                                
                            if not medicamento_alterar:
                                print("Medicamento não encontrado. Tente novamente.")
                                nome_medicamento = input('Digite o nome do medicamento que deseja alterar:\n')

                        print(f"Editando medicamento: {medicamento_alterar.nome}")

                        print('1 - Alterar nome do medicamento\n2 - Alterar principal composto do medicamento\n3 - Alterar laboratório do medicamento')
                        print('4 - Alterar descrição do medicamento\n5 - Alterar valor do medicamento')

                        user_choice_alterarmedic = input('Por favor, escolha o número da ação desejada:\n ')

                        if user_choice_alterarmedic == '1':
                            novo_nome = input(f"Novo nome ({medicamento_alterar.nome}): ")
                            if novo_nome:
                                medicamento_alterar.nome = novo_nome
                                print("Nome do medicamento alterado")
                    
                        if user_choice_alterarmedic == '2':
                            novo_principal_composto = input(f"Novo principal composto ({medicamento_alterar.principal_composto}): ")
                            if novo_principal_composto:
                                medicamento_alterar.principal_composto = novo_principal_composto
                                print ("Principal composto do medicamento alterado")
                    
                        if user_choice_alterarmedic == '3':
                            novo_laboratorio = input(f"Novo laboratório ({medicamento_alterar.laboratorio.nome}): ")
                            lab_associado = Laboratorio.verifica_laboratorio(novo_laboratorio)
                            if lab_associado:
                                medicamento_alterar.laboratorio = lab_associado
                                print ("Laboratório do medicamento alterado")
                    
                        if user_choice_alterarmedic == '4':
                            nova_descrição = input(f"Nova descrição ({medicamento_alterar.descricao}): ")
                            if nova_descrição:
                                medicamento_alterar.descricao = nova_descrição
                                print ("Descrição do medicamento alterada")
                    
                        if user_choice_alterarmedic == '5':
                            novo_valor = float(input(f"Novo valor do medicamento ({medicamento_alterar.valor}): "))
                            if novo_valor:
                                medicamento_alterar.valor = novo_valor
                                print ("Valor do medicamento alterado")

                    elif user_choice_medicamento == '3': #Buscar medicamento
                        try:
                            print('1 - Buscar medicamento por nome\n2 - Buscar medicamento por laboratório\n3 - Buscar medicamento por descrição')
                            user_choice_busca = input('Por favor, escolha o número da ação desejada:\n ')
                            if user_choice_busca == '1':
                                termo_busca = input("Digite o nome do medicamento: ")
                                resultados = [med for med in Medicamentos.lista_medicamentos if termo_busca.lower() in med.nome.lower()]
                                if resultados:
                                    print("Resultados encontrados:")
                                    for med in resultados:
                                        print(med)
                                else:
                                    print("Nenhum resultado encontrado.")
                            elif user_choice_busca == '2':
                                termo_busca = input("Digite o nome do laboratório do medicamento: ")
                                resultados = [med for med in Medicamentos.lista_medicamentos if termo_busca.lower() in med.laboratorio.nome.lower()]
                                if resultados:
                                    print("Resultados encontrados:")
                                    for med in resultados:
                                        print(med)
                                else:
                                    print("Nenhum resultado encontrado.")
                            elif user_choice_busca == '3':
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
                    else:
                        print("Opção inexistente")                  
            
            elif user_choice == '3': # Iniciar Venda 
                try:
                    pass
                except:
                    print('Impossível, nenhum cadastro encontrado!\n')      
            
            elif user_choice == '4': # Emitir Relatórios
                print('1 - Listar clientes\n2 - Listar medicamentos\n3 - Estatísticas das vendas')
                user_choice_relatorio = input('Por favor, escolha o número da ação desejada:\n ')
                if user_choice_relatorio == '1':  # Listar clientes
                    try:
                        cadastro_instance.exibe_clientes(cadastros_clientes)  #Exibir clientes 
                    except:
                        print('Impossível, nenhum cadastro encontrado!\n')
                elif user_choice_relatorio == '2':  # Listar medicamentos
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
                elif user_choice_relatorio == '3':  # Listar estatísticas das vendas
                    pass
                else:
                    print("Opção inexistente")         

if __name__ == '__main__':
    sys()