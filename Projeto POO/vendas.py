from datetime import datetime
from functools import reduce
from cadastra_cliente import Cadastro
from medicamentos import Medicamentos

# por NWErickSasaki
# TODO adicionar get ou property em dados sensiveis
class Vendas:

    def __init__(self) -> None:
        self.data_hora = datetime.now()
        self.carrinho = {} # AKA carrinho { nome_do_medicamento_A : {'qtd':2 , 'valor':'9.90'} }
        self.produtos_vendidos = {} # destinado para relatorio >> apenas nomes e qtds vendidas
        self.valor_total = 0.0
        self.cliente = {}
        return None

    def iniciar_vendas(self) -> None:

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

    def encontrar_cpf_cadastrado(self) -> str:
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

    def fechamento_compra(cpf:int, carrinho:dict) -> None:
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


class carrinho_de_vendas:

    def __init__(self):
        self.carrinho = {}
        _valor_total = 0

    def __repr__(self) -> str: # TODO
        print("""
        01 x Remedio A - R$ 120.00
        03 x Remedio B - R$ 9.90
        ----------------------------
        Total = R$ 149.70
        """)


    def editar_carrinho(self) -> dict:
        opcao = ""
        while not opcao == "0":
            print('\n#'*30,'CARRINHO DE COMPRAS','#'*30)
            opcao = input("""
                    Digite o número correspondente para:
                        
                    1 Visualizar carrinho
                    2 Adicionar um novo item
                    3 Alterar quantidade de um item
                    4 Retirar item do carrinho
                    0 Finalizar venda
                    """)
            match opcao:
                case '1':
                    print(self)

                case '2':
                    #remedio_a_add = Medicamentos
                    #localiza_remedio_por_input()
                    #verifica_se_precisa_de_receita()
                    pass

                case '3':
                    # Se reduzir a zero, deleta do carrinho
                    pass
                
                case '4':
                    pass

                case '0':
                    pass

                case _:
                    print(f"A opcao '{opcao}' é invalida!")
        """
        Atualiza o valor self.valor_total
            
        saída esperada:
        {'Remedio A': {'Preço':120.00, 'Qtd':1} ,
         'Remedio B': {'Preço':9.90, 'Qtd':3}  }
        """
        pass

    @property
    def valor_total(self) -> float:
        soma = lambda element , inicio : element + inicio
        self._valor_total = reduce(soma, (self.carrinho[itens]['Preço']*self.carrinho[itens]['Qtd'] for itens in self.carrinho) , 0)
        return self._valor_total

    def localiza_remedio_por_input(self):
        # Input
        # Se for um remedio Quimioterápicos, alerta para verificar se há receita
        # Se já existe no carrinho, apenas acrescentar + quantidade a ele
        pass


 # Teste ----------------------------------------------------------

teste = True
if(teste):
    novo_carrinho = carrinho_de_vendas()
    novo_carrinho.carrinho = {'Remedio A': {'Preço':120.00, 'Qtd':1} ,
                             'Remedio B': {'Preço':9.90, 'Qtd':3}  }
    print(novo_carrinho.valor_total)