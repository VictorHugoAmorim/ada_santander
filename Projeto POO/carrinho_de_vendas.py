class Carrinho_de_vendas:

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
                    novo_remedio = Medicamentos()
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
    #novo_carrinho = carrinho_de_vendas()
    #novo_carrinho.carrinho = {'Remedio A': {'Preço':120.00, 'Qtd':1} ,
    #                         'Remedio B': {'Preço':9.90, 'Qtd':3}  }
    #print(novo_carrinho.valor_total)
    print(Medicamentos.lista_medicamentos)