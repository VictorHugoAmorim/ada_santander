#Variável global que inicializa o dicionário de cadastros
cadastros_clientes = {
    'identificador': [],
    'nome': [],
    'data_nascimento': []
}
class Cadastro:

    def __init__(self, identificador: str, nome: str, data_nascimento: str) -> None:
        self.identificador , self.nome, self.data_nascimento = self.coleta_dados()

    def coleta_dados(self):
        """
        Nesta função será coletado a partir da exigencias de formatação específicas de cada método
        """
        print('#'*30,'CADASTRO DE CLIENTES','#'*30)
        identificador = self.valida_identificador()
        nome = self.valida_nome()
        data_nascimento = self.valida_data()
        return identificador, nome, data_nascimento

    def armazena_dados(self):
        """
        Nesta função serão armazenados os dados coletados da função 'coleta_dados'.
        Logo após, serão adicionadas a uma estrutura de dicionário.
        """
        cadastros_clientes['identificador'].append(self.identificador)
        cadastros_clientes['nome'].append(self.nome)
        cadastros_clientes['data_nascimento'].append(self.data_nascimento)
        return cadastros_clientes
    
    def valida_identificador(self):
        """
        Validador para identificação, insiste que o usuário digite a quantidade e formato correto
        """
        while True:
            identificador = input('Digite o CPF: [Apenas números - 11 dígitos]\n').strip()
            if identificador.isdigit() and len(identificador) == 11:
               break
            else:
                print('Formato de CPF inválido')
        return identificador
    
    def valida_nome(self):
        while True:
            nome = input('Digite o nome:\n').strip().upper()
            if len(nome) > 0 and nome.isprintable() and nome.isdigit() == False:
                break
        return nome
    
    def valida_data(self):
        while True:
            print('Por favor, forneça sua data de nascimento:\n')
            dia = input('Digite o dia do nascimento: [dd]\n').strip()
            mes = input('Digite o mês do nascimento: [mm]\n').strip()
            ano = input('Digite o ano do nascimento: [aaaa]\n').strip()
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                data_nascimento = f'{dia:02d}/{mes:02d}/{ano:04d}'
                break
            else:
                print('Formato de data inválido\n')
        return data_nascimento

    def altera_cliente(self, cadastros_clientes):
        cadastros_clientes = cadastros_clientes
        print('#'*30,'ALTERAÇÕES DE CLIENTES','#'*30)
        while True:
            cliente_escolhido = input('Digite o CPF do cliente [Apenas números - 11 dígitos] ou enter para sair:\n').strip()
            if cliente_escolhido in cadastros_clientes['identificador']:
                idx = cadastros_clientes['identificador'].index(cliente_escolhido)
                print(f'cliente {cadastros_clientes["nome"][idx]} encontrado')
                escolha_alteracao = input('Escolha qual campo deseja alterar:\n1-CPF:\n2-Nome:\n3-Data de Nascimento:\n4-Sair:\n').strip()
                if escolha_alteracao == '4':
                    break
                elif escolha_alteracao == '1':
                    novo_cpf = self.valida_identificador()
                    cadastros_clientes['identificador'][idx] = novo_cpf
                    print(f'Cliente {cadastros_clientes["nome"][idx]} agora possui o CPF: {cadastros_clientes["identificador"][idx]}')
                elif escolha_alteracao == '2':
                    novo_nome = self.valida_nome()
                    cadastros_clientes['nome'][idx] = novo_nome
                    print(f'Cliente {cadastros_clientes["nome"][idx]} teve seu nome atualizado')
                elif escolha_alteracao == '3':
                    nova_data = self.valida_data()
                    cadastros_clientes['data_nascimento'][idx] = nova_data
                    print(f'Cliente {cadastros_clientes["nome"][idx]} agora possui a data de nascimento: {cadastros_clientes["data_nascimento"][idx]}')
            else:
                if len(cadastros_clientes) > 0:
                    print('CPF incorreto ou não cadastrado')
                break

    def exibe_clientes(self, cadastros_clientes):
        print('#'*30,'EXIBIÇÃO DE CLIENTES','#'*30)
        cadastros_clientes = cadastros_clientes
        num_clientes = len(cadastros_clientes['identificador'])
        for i in range(num_clientes):
            print(f"CPF: {cadastros_clientes['identificador'][i]}")
            print(f"nome: {cadastros_clientes['nome'][i]}")
            print(f"data_nascimento: {cadastros_clientes['data_nascimento'][i]}\n")

    @staticmethod
    def exec():
        cadastro = Cadastro('','','')
        cadastros_clientes = cadastro.armazena_dados()
        cadastro.armazena_dados()
        cadastro.altera_cliente(cadastros_clientes)

if __name__ == "__main__":
    cadastros = Cadastro.exec()