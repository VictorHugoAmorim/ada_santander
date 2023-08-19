from datetime import datetime
from cadastra_cliente import *
from cadastra_cliente import Cadastro
from medicamentos import Medicamentos
from carrinho_de_vendas import Carrinho_de_vendas

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

    def atualiza_valores(self) -> None:
        self._valor_total_sem_desconto = self.produtos_vendidos.valor_total
        self._porcentagem_de_desconto = self.verifica_porcentagem_de_desconto( self.cliente['idade'] , self._valor_total_sem_desconto )
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
        self.cliente = self.encontrar_cliente_por_cpf()
        self.produtos_vendidos  = Carrinho_de_vendas().editar_carrinho()
        #self._valor_total_sem_desconto = self.produtos_vendidos.valor_total 
        #self.porcentagem_de_desconto = self.verifica_porcentagem_de_desconto( self.cliente['idade'] , self._valor_total_sem_desconto )
        
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

    

    def verifica_porcentagem_de_desconto( idade:int , total_da_compra:float ) -> float:
        return DESCONTO_PORCENTAGEM_IDOSO if idade > IDADE_IDOSO else DESCONTO_PORCENTAGEM_COMPRA_GRANDE if total_da_compra > VALOR_COMPRA_GRANDE else 0

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