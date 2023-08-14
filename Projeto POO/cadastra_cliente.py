
class Cadastro:

    def __init__(self, identificador: str, nome: str, data_nascimento: str) -> None:
        self.identificador , self.nome, self.data_nascimento = self.coleta_dados()

    def coleta_dados(self):
        """
        Nesta função será coletado os dados enqunto se verifica as entrada possíveis entradas incorretas do usuário.
        O código mantem redundancia das coletas até que o usuário forneça uma entrada válida
        """
        while True:
            identificador = input('Digite o CPF: [Apenas números - 11 dígitos]\n').strip()
            if identificador.isdigit() and len(identificador) == 11:
               break
            else:
                print('Formato de CPF inválido')
        while True:
            nome = input('Digite o nome:\n').strip().upper()
            if len(nome) > 0 and nome.isprintable() and nome.isdigit() == False:
                break
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
        return identificador, nome, data_nascimento

    def armazena_dados(self):
        """
        Nesta função serão armazenados os dados coletados da função 'coleta_dados'.
        Logo após, serão adicionadas a uma estrutura de dicionário.
        """
        cadastros_clientes = {
            'identificador': [],
            'nome': [],
            'data_nascimento': []
        }
        cadastros_clientes['identificador'].append(self.identificador)
        cadastros_clientes['nome'].append(self.nome)
        cadastros_clientes['data_nascimento'].append(self.data_nascimento)
        return cadastros_clientes
    
    @staticmethod
    def exec():
        cadastro = Cadastro('','','')
        cadastros_clientes = cadastro.armazena_dados()
        return cadastros_clientes

if __name__ == "__main__":
    cadastros = Cadastro.exec()
    print(cadastros)