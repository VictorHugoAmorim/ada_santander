from datetime import datetime
from cadastra_cliente import *
from cadastra_cliente import Cadastro
from medicamentos import Medicamentos
from carrinho_de_vendas import Carrinho_de_vendas

# by NWErickSasaki
# TODO sigilo no valor do carrinho, cliente na compra, CPF do cliente
class Vendas:

    cadastro_vendas=[] # [ [ cliente.Cadastro() , datetime.now() , carrinho.Carrinho() ] , [...] ]

    def __init__(self, cliente:Cadastro=Cadastro(), data_hora:datetime=datetime.now(),produtos_vendidos:Carrinho_de_vendas=Carrinho_de_vendas()) -> None:
        self.cliente = self.cliente
        self.data_hora = self.data_hora
        self.produtos_vendidos = self.produtos_vendidos
        self._valor_total = self.calcula_total( self.produtos_vendidos ) 
        self.desconto = self.verifica_desconto( self.cliente['idade'] , self.produtos_vendidos.valor_total )
        return None

    @property
    def valor_total(self):
        return self._valor_total

    def iniciar_vendas(self) -> None: # TODO
        self.cliente = self.encontrar_cliente_por_cpf()
        self.produtos_vendidos  = Carrinho_de_vendas().editar_carrinho()
        self.valor_total = self.calcula_total( self.produtos_vendidos ) 
        self.desconto = self.verifica_desconto( self.cliente['idade'] , self.produtos_vendidos.valor_total )
        
        self.fechamento_compra() 
        return None

    def encontrar_cliente_por_cpf(self) -> Cadastro: # TODO

        # cpf = input_de_CPF_valido() TODO

        if cpf not in Cadastro.cadastros_clientes['identificador']:
            opcao = input("""
                  CPF não encontrado no sistema.
                  Digite o número correspondente para: 
                  1 - Buscar outro CPF
                  2 - Cadastrar o novo cliente
                  """)
            match opcao:
                case '1':

                    cpf = input_de_CPF_valido() # TODO

                    pass
                    #cpf = input_de_CPF_valido() # TODO

                case '2':
                    pass
                    #cliente.Cadastro.coleta_dados()
                case _:
                    pass
        # return cliente_com_cpf(cpf) TODO

    

    def verifica_desconto( idade:int , total_da_compra:float ) -> float:
        return 0.2 if idade > 65 else 0.1 if total_da_compra > 150 else 0

    def fechamento_compra() -> None: # TODO
        """
        Ao fechar adiciona a compra ao "banco de dados"
        em formato dict usando como chave o datetime
        e adiciona no arquivo .json 
        """
        self.valor_total = self.produtos_vendidos.valor_total-desconto
        print(f"""
            ----- COMPRA CADASTRADA -----  

            CLIENTE {self.cliente.nome}
            CPF {cliente.identificador}
            {self.produtos_vendidos}
            DESCONTO/tR$ {desconto:.2f}
            TOTAL A PAGAR R$ {(valor_total):.2f}
            -----------------------------""")

        pass

teste = True
if teste:
    nv = Vendas()
    print(nv)