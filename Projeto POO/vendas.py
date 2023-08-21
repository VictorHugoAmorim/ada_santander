from datetime import datetime
from cadastra_cliente import *
from cadastra_cliente import Cadastro
from medicamentos import Medicamentos
from carrinho_de_vendas import Carrinho_de_vendas
from datetime import date
import csv

IDADE_IDOSO = 65
VALOR_COMPRA_GRANDE = 150
DESCONTO_PORCENTAGEM_IDOSO = 0.2
DESCONTO_PORCENTAGEM_COMPRA_GRANDE = 0.1

# by NWErickSasaki
# TODO sigilo no valor do carrinho, cliente na compra, CPF do cliente
class Vendas:

    cadastro_vendas=[] # [ obj_vendas1, obj_vendas2 ]

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
        if (novo_valor*self.porcentagem_de_desconto == novo_valor*DESCONTO_PORCENTAGEM_IDOSO and self.cliente.idade > IDADE_IDOSO) or (novo_valor*self.porcentagem_de_desconto == novo_valor*DESCONTO_PORCENTAGEM_COMPRA_GRANDE and self._valor_total_sem_desconto > VALOR_COMPRA_GRANDE):
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
        print(self)
        Vendas.salva_banco(self)
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
        #return Cadastro._cliente_que_contenha_o_cpf(cpf)
        return Cadastro('12345678901','Erick Teste', date(2000,1,1)) # para usar para teste enquanto a função acima for implementada

    def verifica_porcentagem_de_desconto( idade:int , total_da_compra:float ) -> float:
        return DESCONTO_PORCENTAGEM_IDOSO if idade > IDADE_IDOSO else DESCONTO_PORCENTAGEM_COMPRA_GRANDE if total_da_compra > VALOR_COMPRA_GRANDE else 0

    def fechamento_compra(self) -> None: # TODO
        self.atualiza_valores()
        Vendas.cadastro_vendas.append(self)
        return None

    def salva_banco(self) -> None:
        str_de_produtos = ','.join([e.nome for e in self.produtos_vendidos.carrinho[0]])
        str_de_precos = ','.join([str(e) for e in self.produtos_vendidos.carrinho[1]])
        try:
            PATH = '.\csv\'
            f = open(f'{PATH}vendas.csv','a', encoding='utf-8')
        except:
            PATH = 'Projeto POO/csv/'
            f = open(f'{PATH}vendas.csv','a', encoding='utf-8')
        f.write(f'\n{self.cliente.nome};{self.data_hora};{str_de_produtos};{str_de_precos}')
        f.close()
        return None

    def carrega_banco(self) -> None:
        try:
            PATH = '.\csv\'
            f = open(f'{PATH}vendas.csv','r', encoding='utf-8')
        except:
            PATH = 'Projeto POO/csv/'
            f = open(f'{PATH}vendas.csv','r', encoding='utf-8')
        conteudo = csv.DictReader(f)
        for linha in conteudo:
            cpf = linha['IDENTIFICADOR']
            # cliente = Cadastro.pega_cliente_com_cpf(cpf) # TODO
            data_hora = linha['DATA_HORA']
            lista_produtos = linha['PRODUTOS'].split(',')
            #obj_produtos = [ tranforma_em_obj(nome_produtos) for nome_produtos in lista_produtos ] # TODO
            quantidade = linha['QUANTIDADE'].split(',')
            # novo_carrinho = Carrinho_de_vendas([ obj_produtos , quantidade ]) # TODO
            # nova_venda = Vendas(cliente, data_hora, novo_carrinho) # TODO
            # cadastro_vendas.append(nova_venda) # TODO
        f.close()
        return None

# Teste ----------------------------------------------------------

TESTE = 0
if TESTE:
    import lendocsv
    lendocsv.lendo_csv()
    #Vendas.carrega_banco()
    print('\n\n VOCE ESTA RODANDO UM TESTE \n\n')
    eu = Cadastro('12345678901','Erick Teste', date(2000,1,1))
    eu.armazena_dados()

    #print(eu.nome)
    #print(eu.identificador)
    #print(eu.data_nascimento)

    nv = Vendas()
    #print(nv)
    nv.iniciar_vendas()