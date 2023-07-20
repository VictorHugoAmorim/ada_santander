from collections import namedtuple

Pessoa = namedtuple('Pessoa', ['cpf', 'nome', 'idade', 'sexo', 'renda', 'estado'])

def cadastrar_usuario():
    continuar_cadastro = True
    cadastros = {}

    while continuar_cadastro:
        cadastrar = input('Deseja inserir um novo cadastro? ')
        if cadastrar.lower() in ['sim', 's', 'yes', 'y']:
            cpf = input('Insira o cpf: ')
            nome = input('Insira o nome: ')
            idade = int(input('Insira a idade: '))
            sexo = input('Insira o sexo: ')
            renda = float(input('Insira a renda: '))
            estado = input('Insira o estado: ')
            cadastro = Pessoa(cpf=cpf, nome=nome, idade=idade, sexo=sexo, renda=renda, estado=estado)
            cadastros[cpf] = cadastro
        elif cadastrar.lower() in ['não', 'n', 'nao', 'no']:
            print(f'Cadastro finalizado, inserido {len(cadastros)} novos')
            continuar_cadastro = False
        else:
            print(f'Opção inválida. Foi inserido "{cadastrar}", escolha entre [sim, s, yes, y] para cadastrar uma nova pessoa ou [não, nao, n, no] para parar')

    return cadastros

def calcule_media_idade_por_sexo(cadastros):
    total_masc = 0
    total_fem = 0
    qtd_masc = 0
    qtd_fem = 0

    for cpf, pessoa in cadastros.items():
        if pessoa.sexo.lower() == 'm':
            total_masc += pessoa.idade
            qtd_masc += 1
        elif pessoa.sexo.lower() == 'f':
            total_fem += pessoa.idade
            qtd_fem += 1

    media_masc = total_masc / qtd_masc if qtd_masc > 0 else 0
    media_fem = total_fem / qtd_fem if qtd_fem > 0 else 0

    return (('m', media_masc), ('f', media_fem))

def conte_quantidade_por_sexo(cadastros):
    qtd_masc = 0
    qtd_fem = 0

    for pessoa in cadastros.values():
        if pessoa.sexo.lower() == 'm':
            qtd_masc += 1
        elif pessoa.sexo.lower() == 'f':
            qtd_fem += 1

    return (('m', qtd_masc), ('f', qtd_fem))


def filtre_dados(cadastros, estado):
    cadastros_filtrado = {}
    for cpf, pessoa in cadastros.items():
        if pessoa.estado.lower() == estado.lower():
            cadastros_filtrado[cpf] = pessoa
    return cadastros_filtrado

def delete_cadastro(cadastros, cpf):
    if cpf in cadastros:
        del cadastros[cpf]
        return True
    else:
        return False

# Executando as funções
cadastros = cadastrar_usuario()
print(cadastros)

media_idade_por_sexo = calcule_media_idade_por_sexo(cadastros)
print("Média de idade por sexo:", media_idade_por_sexo)

quantidade_por_sexo = conte_quantidade_por_sexo(cadastros)
print("Quantidade de pessoas por sexo:", quantidade_por_sexo)

estado_filtro = input("Digite o estado para filtrar os dados: ")
cadastros_filtrado = filtre_dados(cadastros, estado_filtro)
print("Cadastro filtrado por estado:", cadastros_filtrado)

cpf_delete = input("Digite o CPF para deletar o cadastro: ")
delete_result = delete_cadastro(cadastros, cpf_delete)
if delete_result:
    print("Cadastro deletado com sucesso.")
else:
    print("CPF não encontrado, nenhum cadastro foi deletado.")