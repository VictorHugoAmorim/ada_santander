from datetime import datetime
from cadastra_cliente import *
from cadastra_cliente import Cadastro
from medicamentos import Medicamentos
from carrinho_de_vendas import Carrinho_de_vendas
from datetime import date

IDADE_IDOSO = 65
VALOR_COMPRA_GRANDE = 150
DESCONTO_PORCENTAGEM_IDOSO = 0.2
DESCONTO_PORCENTAGEM_COMPRA_GRANDE = 0.1

# by NWErickSasaki
# TODO sigilo no valor do carrinho, cliente na compra, CPF do cliente
class Vendas:

    cadastro_vendas=[] # [ [ cliente.Cadastro() , datetime.now() , carrinho.Carrinho() ] , [...] ]

    def __init__(self, cliente:Cadastro=Cadastro(), data_hora:datetime=datetime.now(), produtos_vendidos:Carrinho_de_vendas=Carrinho_de_vendas()) -> None:
        self.cliente = cliente
        self.data_hora = data_hora
        self.produtos_vendidos = produtos_vendidos
        self.atualiza_valores()
        return None

    def __repr__(self):
        return(f"""
        \t############################################################  

        \tCLIENTE\t{self.cliente.nome.upper()}
        \tCPF\t{self.cliente.identificador}
        {self.produtos_vendidos}
        \tDESCONTO\tR$ {self._valor_de_desconto:.2f}\t({self._porcentagem_de_desconto*100:.2f}%)
        \tTOTAL A PAGAR \tR$ {(self._valor_total_com_desconto):.2f}

        \t############################################################""")

    def atualiza_valores(self) -> None:
        self._valor_total_sem_desconto = self.produtos_vendidos.valor_total
        self._porcentagem_de_desconto = Vendas.verifica_porcentagem_de_desconto( self.cliente.idade , self._valor_total_sem_desconto )
        self._valor_de_desconto = self.porcentagem_de_desconto * self._valor_total_sem_desconto
        self._valor_total_com_desconto = self._valor_total_sem_desconto - self.valor_de_desconto
        return None

    @property
    def valor_total_sem_desconto(self):
        self._valor_total_sem_desconto = self.produtos_vendidos.valor_total
        return self._valor_total_sem_desconto

    @property
    def porcentagem_de_desconto(self):
        return self._porcentagem_de_desconto
    
    @porcentagem_de_desconto.setter
    def porcentagem_de_desconto(self, porcentagem):
        if (porcentagem == DESCONTO_PORCENTAGEM_IDOSO and self.cliente.idade > IDADE_IDOSO) or (porcentagem == DESCONTO_PORCENTAGEM_COMPRA_GRANDE and self._valor_total_sem_desconto > VALOR_COMPRA_GRANDE):
            self._porcentagem_de_desconto = porcentagem
        else:
            print("ALERTA! Porcentagem de desconto nao autorizado!")

    @property
    def valor_de_desconto(self):
        return self._valor_de_desconto

    @valor_de_desconto.setter
    def valor_de_desconto(self, novo_valor):
        if (novo_valor*self.porcentagem_de_desconto == novo_valor*DESCONTO_PORCENTAGEM_IDOSO and self.cliente.idade > IDADE_IDOSO) or (novo_valor*self.porcentagem_de_desconto == valor*DESCONTO_PORCENTAGEM_COMPRA_GRANDE and self._valor_total_sem_desconto > VALOR_COMPRA_GRANDE):
            self._valor_de_desconto = novo_valor
        else:
            print("ALERTA! Valor de desconto nao autorizado!")

    @property
    def valor_total_com_desconto(self):
        self._valor_total_com_desconto = self._valor_total_sem_desconto - self.valor_de_desconto
        return self._valor_total_com_desconto

    def iniciar_vendas(self) -> None: # TODO
        print("Para realizar uma venda, por favor, informe o cliente.")
        self.cliente = self.encontrar_cliente_por_cpf()
        print(f"\nCliente localizado. \nBem vindo {self.cliente.nome} \nnIniciando venda.")
        self.produtos_vendidos  = Carrinho_de_vendas().editar_carrinho()       
        self.fechamento_compra() 
        return None

    def encontrar_cliente_por_cpf(self) -> Cadastro: # TODO
        cpf = Cadastro.valida_identificador()
        while cpf not in cadastros_clientes['identificador']:
            opcao = input("""
                  CPF não encontrado no sistema.
                  Digite o número correspondente para: 
                  1 - Cadastrar cliente
                  * - Buscar outro CPF
                  """)
            match opcao:
                case '1':
                    novo_cliente = Cadastro(Cadastro.coleta_dados())
                    novo_cliente.armazena_dados()
                    cpf = novo_cliente.identificador
                case _:
                     cpf = Cadastro.valida_identificador()
        return Cadastro._cliente_que_contenha_o_cpf(cpf)
        #return Cadastro('12345678901','Erick Teste', date(2000,1,1)) # para usar para teste enquanto a função acima for implementada

    def verifica_porcentagem_de_desconto( idade:int , total_da_compra:float ) -> float:
        return DESCONTO_PORCENTAGEM_IDOSO if idade > IDADE_IDOSO else DESCONTO_PORCENTAGEM_COMPRA_GRANDE if total_da_compra > VALOR_COMPRA_GRANDE else 0

    def fechamento_compra(self) -> None: # TODO
        """
        Ao fechar adiciona a compra ao "banco de dados"
        em formato dict usando como chave o datetime
        e adiciona no arquivo .json 
        """
        self.atualiza_valores()
        print(self)

        pass

# Teste ----------------------------------------------------------

TESTE = 0
if TESTE:
    import lendocsv
    lendocsv.lendo_csv()
    print('\n\n VOCE ESTA RODANDO UM TESTE \n\n')
    eu = Cadastro('12345678901','Erick Teste', date(2000,1,1))
    eu.armazena_dados()

    #print(eu.nome)
    #print(eu.identificador)
    #print(eu.data_nascimento)

    nv = Vendas()
    #print(nv)
    nv.iniciar_vendas()