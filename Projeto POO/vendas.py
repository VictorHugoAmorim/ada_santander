from datetime import datetime
class Vendas:
    def __init__(self) -> None:
        self.data_hora = datetime.now()
        self.produtos_vendidos = []
        self.valor_total = 0.0
        self.cliente = {}
        return None

    def iniciar_vendas() -> None:
        pass
        # Verifica se o cliente é cadastrado
        if not self.cliente:
            verifica_cliente()

        # Inclui medicamento que o cliente quer comprar
        self.produtos_vendidos = formar_carrinho()

        # Verifica quanto de desconto o cliente tem
        desconto:float = verifica_desconto(cpf) 

        # Fecha compra com valor total
        fechamento_compra(cpf, carrinho_de_compra)


    def verifica_cliente() -> dict:
        """
        Entra com CPF ou Nome do cliente (e lista clientes que possuem esse mesmo nome digitado)
        Se não for encontrado, alerta e orientado para cadastrar cliente
        Se encontrado retorna o CPF em int
        """
        pass
        #info_cliente = input('Digite o CPF (sem pontucao) ou nome do cliente: ')
        # Se CPF

        # Se nome
    
    def formar_carrinho() -> list:
        """
        entra com medicamentos no carrinho até usuário sair.
        se for um remedio Quimioterápicos, alerta para verificar se há receita
        """
        pass

    def fechamento_compra(cpf:int, lista_de_compra:list) -> None:
        """
        mostra lista de medicamentos, valores unitários
        mostra valor total (sem desconto)
        mostra desconto
        mostra valor a pagar
        """
        pass

"""
Apenas para clientes cadastrados -> if cliente.CPF or cliente.Nome:
20% de desconto para clientes idosos (acima de 65 anos) if cliente.idade > 65:
10% de desconto nas compras acima de 150 reais ... medic_quimio.Valor_de_venda ... medic_fit.Valor_de_venda 
Se Quimioterápicos for do tipo controlado, exige receita, emite alerta perguntando se o atendente verificou if medic_quimio.Necessita_receita
Arquivo .json contendo um exemplo de cadastros cadastros_vendas = {}
Classe Vendas (data_hora, produtos_vendidos, cliente, valor_total)
"""