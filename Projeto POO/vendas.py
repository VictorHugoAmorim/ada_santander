class Vendas:
    def __init__(self, data_hora: str, produtos_vendidos: str, cliente: str, valor_total: float) -> None:
        self.data_hora = data_hora
        self.produtos_vendidos = produtos_vendidos
        self.cliente = cliente
        self.valor_total = valor_total
        