from datetime import datetime
from cadastra_cliente import Cadastro
from medicamentos import Medicamentos
from carrinho_de_vendas import Carrinho_de_vendas

# by NWErickSasaki
# TODO adicionar get ou property em dados sensiveis
class Vendas:

    def __init__(self) -> None:
        self.data_hora = datetime.now()
        self.produtos_vendidos = {} # destinado para relatorio >> apenas nomes e qtds vendidas
        self.valor_total = 0.0
        self.cliente = {}
        return None

    def iniciar_vendas(self) -> None: # TODO

        cpf = self.encontrar_cpf_cadastrado()
        
        # Inclui medicamento que o cliente quer comprar
        self.produtos_vendidos = self.editar_carrinho()

        # Verifica quanto de desconto o cliente tem
        self.valor_total = self.calcula_total( self.produtos_vendidos )
        desconto:float = self.verifica_desconto( self.cliente['idade'] , sum( self.valores_produtos) ) 

        # Fecha compra com valor total
        self.fechamento_compra( self.cliente[cpf], self.produtos_vendidos_de_compra )

        # Volta ao menu principal da farmacia  
        return None

    def encontrar_cpf_cadastrado(self) -> str: # TODO
        cliente = Cadastro('','','')
        cpf = cliente.Cadastro.valida_identificador() # so inserir CPF valido
        if cpf not in cliente.Cadastro.cadastros_clientes['identificador']:
            opcao = input("""
                  CPF não encontrado no sistema.
                  Digite o número correspondente para: 
                  1 - Buscar outro CPF
                  2 - Cadastrar o novo cliente
                  * - Sair
                  """)
            match opcao:
                case '1':
                    cpf = cliente.Cadastro.valida_identificador()
                case '2':
                    cliente.Cadastro.coleta_dados()
                    cpf = cliente.Cadastro.cadastros_clientes['identificador']
                case _:
                    return None
        return cpf

    def verifica_desconto( idade:int , total_da_compra:float ) -> float:
        return 0.2 if idade > 65 else 0.1 if total_da_compra > 150 else 0

    def fechamento_compra(cpf:int, carrinho:dict) -> None: # TODO
        """
        mostra a revisão do produtos_vendidos:
            mostra lista de medicamentos, valores unitários
            mostra valor total (sem desconto)
            mostra desconto
            mostra valor a pagar
            pergunta se esta tudo certo
        permite editar o produtos_vendidos e recalcula:
            o valor de desconto
            o valor total
            retorna a revisão:

        ao fechar adiciona a compra ao "banco de dados"
        em formato dict usando como chave o datetime
        e adiciona no arquivo .json 
        """
        pass