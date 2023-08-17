from medicamentos import Medicamentos
from medic_fit import MedicFit
from medic_quimio import MedicQuimio
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
                    lista_de_remedio = self.localiza_remedio_por_input() # retorna uma lista
                    # remedio_selecionado = pega_um(lista_de_remedio) 
                    # verifica_se_precisa_de_receita(remedio_selecionado)
                    #   isinstance (remedio_selecionado, MedicQuimio)
                    #        if remededio_selecionado.necessita_receita
                    #        print("Verique se tem receita")
                    #adiciono o remedio ao carrinho
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




    def localiza_remedio_por_input(self,palavra_do_remedio:str="") -> Medicamentos:
        if not palavra_do_remedio:
            palavra_do_remedio =  input('Qual remedio está procurando?')
        palavra_do_remedio = palavra_do_remedio.lower()
        lista_remedios_por_nome = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.nome.lower()]
        lista_remedios_por_principal_composto = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.principal_composto.lower()]
        #lista_remedios_por_laboratorio = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.laboratorio.nome.lower()]
        lista_remedios_por_descricao = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.descricao.lower()]

        #lista_todos = lista_remedios_por_nome + lista_remedios_por_principal_composto + lista_remedios_por_laboratorio + lista_remedios_por_descricao

        lista_todos = lista_remedios_por_nome + lista_remedios_por_principal_composto  + lista_remedios_por_descricao
        dict_remedios={}
        for e in lista_todos:
            dict_remedios[e.nome] = e

        return list(dict_remedios)





        # Se for um remedio Quimioterápicos, alerta para verificar se há receita
        # Se já existe no carrinho, apenas acrescentar + quantidade a ele
        pass


 # Teste ----------------------------------------------------------

teste = True
if(teste):
    nc = Carrinho_de_vendas()
    #nc.carrinho = {'Remedio A': {'Preço':120.00, 'Qtd':1} ,
    #                         'Remedio B': {'Preço':9.90, 'Qtd':3}  }
    #print(nc.valor_total)
    #print(Medicamentos.lista_medicamentos)
    RemedioA=MedicFit('Coristina D',"abc",'aa','b c d e',5)
    RemedioD=MedicQuimio('Coristina E',"abc",'aa','b c d e',5,True)
    RemedioB=MedicFit('Coristina F',"abc",'aa','b c d e',50)
    RemedioC=Medicamentos('Neosaldina',"novalgina",'aa','b c d e',15)
    print(nc.localiza_remedio_por_input('Coristina'))