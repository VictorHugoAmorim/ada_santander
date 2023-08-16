from datetime import datetime
from functools import reduce

class Vendas:
    def __init__(self) -> None:
        self.data_hora = datetime.now()
        self.produtos_vendidos = {} # AKA carrinho { nome_do_medicamento_A : {'qtd':2 , 'valor':'9.90'} }
        self.valor_total = 0.0
        self.cliente = {}
        return None

    def iniciar_vendas() -> None:
        # Verifica se o cliente é cadastrado
        if not self.cliente:
            self.cliente = verifica_cliente()

        # Inclui medicamento que o cliente quer comprar
        self.produtos_vendidos = editar_carrinho()

        # Verifica quanto de desconto o cliente tem
        self.valor_total = calcula_total( self.produtos_vendidos )
        desconto:float = verifica_desconto( self.cliente['idade'] , sum( self.valores_produtos) ) 

        # Fecha compra com valor total
        fechamento_compra( self.cliente[cpf], produtos_vendidos_de_compra )

        # Volta ao menu principal da farmacia
        return


    def verifica_cliente() -> dict:
        """
        Input de CPF ou Nome do cliente (e lista clientes que possuem esse mesmo nome digitado)
        Se não for encontrado, alerta e dá a opção de cadastrar cliente
        
        Se encontrado retorna os dados do cliente em formato dict
        exemplo: {'Nome':'Erick', 'Idade':28}
        """
        pass
    
    def editar_carrinho(carrinho:dict) -> dict:
        """
        Se chamar a função sem parâmetro,
            cria um carrinho vazio

        Se entrar na função já com parametros de entrada,
            permite editar o carrinho existente

        O usuario pode, em relação ao carrinho:
            1 Visualizar
            2 Adicionar um novo item
                Se for um remedio Quimioterápicos, alerta para verificar se há receita
                Se já existe no carrinho, apenas acrescentar + quantidade a ele
            3 Alterar quantidade de um item
                Se reduzir a zero, deleta do carrinho
            4 Retirar item do carrinho
        
        Atualiza o valor self.valor_total
            
        saída esperada:
        {'Remedio_A': {'Nome':'Remedio_A', 'Preço':120.00, 'Qtd':1} ,
         'Remedio_B': {'Nome':'Remedio_B', 'Preço':9.90, 'Qtd':3}  } 
        """
        pass

    def calcula_total(carrinho: dict) -> float:
        """
        Entra com o carrinho atual
        calcula o valor total com base no
        valor unitário * quantidade de item no carrinho

        retorna valor em float. # 120.90
        """
        soma = lambda element , inicio = elemento + inicio
        return reduce(soma, carrinho[itens]['Preço']*carrinho[itens]['Qtd'] for itens in carrinho , 0)
        pass

    def verifica_desconto( idade:int , total:float ) -> float:
        """
        Entra com a idade e valor total da compra
        Se idade do cliente acima de 65 anos
            retorna 0.20
        Se compra acima de 150
            retorna 0.10
        """
        pass 

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
