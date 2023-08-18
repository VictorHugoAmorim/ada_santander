from datetime import datetime
from cadastra_cliente import Cadastro
from medicamentos import Medicamentos
from carrinho_de_vendas import Carrinho_de_vendas

# by NWErickSasaki
# TODO adicionar get ou property em dados sensiveis
class Vendas:

    cadastro_vendas=[] # [ cliente.Cadastro() , datetime.now() , carrinho.Carrinho() ]

    def __init__(self) -> None:
        self.data_hora = datetime.now()
        self.produtos_vendidos:Carrinho_de_vendas
        self.valor_total:float
        self.cliente:Cadastro
        return None

    def iniciar_vendas(self) -> None: # TODO

        cpf = self.encontrar_cpf_cadastrado()
        
        # Inclui medicamento que o cliente quer comprar
        novo_carrinho = Carrinho_de_vendas()
        novo_carrinho = self.editar_carrinho()

        # Verifica quanto de desconto o cliente tem
        self.valor_total = self.calcula_total( self.produtos_vendidos ) 

        # Fecha compra com valor total
        self.fechamento_compra( self.cliente, novo_carrinho )

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

    def fechamento_compra(cliente:Cadastro, carrinho:Carrinho_de_vendas) -> None: # TODO
        """
        Ao fechar adiciona a compra ao "banco de dados"
        em formato dict usando como chave o datetime
        e adiciona no arquivo .json 
        """
        desconto:float = self.verifica_desconto( self.cliente['idade'] , sum( self.valores_produtos) )
        self.valor_total = carrinho.valor_total-desconto
        print(f"""
            ----- COMPRA CADASTRADA -----  

            CLIENTE {cliente.nome}
            CPF {cliente.identificador}
            {carrinho}
            DESCONTO/tR$ {desconto:.2f}
            TOTAL A PAGAR R$ {(valor_total):.2f}
            -----------------------------""")

        pass