from medicamentos import Medicamentos
from medic_fit import MedicFit
from medic_quimio import MedicQuimio

# by NWErickSasaki
class Carrinho_de_vendas:

    def __init__(self):
        self.carrinho = [] # [ [obj_Medicamento , 1 ] , [obj_Medicamento_A , 3 ] ]
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
            print('\n','#'*30,'CARRINHO DE COMPRAS','#'*30)
            opcao = input("""
                    1 Visualizar carrinho
                    2 Adicionar um novo item
                    3 Alterar quantidade de um item
                    4 Retirar item do carrinho
                    0 Finalizar venda
                    
                    Digite um numero: """)
            match opcao:
                case '1':
                    print(self)

                case '2':
                    remedio_selecionado = self.localiza_remedio_por_input()

                    if self.medicamento_ja_no_carrinho(remedio_selecionado):
                        pass # so altera quantidade

                    if self.verifica_se_precisa_de_receita(remedio_selecionado):
                        if not self.cliente_tem_receita_para(remedio_selecionado):
                            print(f'O remedio {remedio_selecionado.nome} nao adicionado ao carrinho.')
                            continue

                    carrinnho.appen###
                    #adiciono o remedio ao carrinho

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

    def cliente_tem_receita_para(remedio_selecionado:Medicamentos) -> bool:
        num = input(f"""
        O Cliente tem receita para
        {remedio_selecionado.nome}?

        1 - Sim
        2 - Não
        * - Voltar
        
        Digite o numero correspondente: """).split()
        return (True if num == "1" else False)






    def verifica_se_precisa_de_receita(self, remedio:Medicamentos)-> bool:
        if isinstance(remedio, MedicQuimio):
            return remedio.necessita_receita
        return False

    def medicamento_ja_no_carrinho(remedio_selecionado:Medicamentos) -> bool:
        if remedio_selecionado in self.carrinho[0]:
            return True
        return False

    @property
    def valor_total(self) -> float:
        soma = lambda element , inicio : element + inicio
        self._valor_total = reduce(soma, (self.carrinho[itens]['Preço']*self.carrinho[itens]['Qtd'] for itens in self.carrinho) , 0)
        return self._valor_total



    def localiza_remedio_por_input(self,palavra_do_remedio:str="") -> Medicamentos:
        if not palavra_do_remedio:
            palavra_do_remedio =  input('Digite qual remedio está procurando:')
        palavra_do_remedio = palavra_do_remedio.lower()
        lista_remedios_por_nome = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.nome.lower()]
        lista_remedios_por_principal_composto = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.principal_composto.lower()]
        lista_remedios_por_descricao = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.descricao.lower()]
        #lista_remedios_por_laboratorio = [ remedio for remedio in Medicamentos.lista_medicamentos if palavra_do_remedio in remedio.laboratorio.nome.lower()]
        
        #lista_todos = lista_remedios_por_nome + lista_remedios_por_principal_composto + lista_remedios_por_laboratorio + lista_remedios_por_descricao
        lista_todos = lista_remedios_por_nome + lista_remedios_por_principal_composto  + lista_remedios_por_descricao
        
        dict_remedios={}
        for e in lista_todos:
            dict_remedios[e] = e
        lista_de_remedio = list(dict_remedios)

        if not lista_de_remedio:
            return False
        elif len(lista_de_remedio)>1:
            return self.escolha_um_remedio_na(lista_de_remedio)
        else:
            return lista_de_remedio[0]

    def escolha_um_remedio_na(self, lista_de_remedio: list) -> Medicamentos:
        print('Digite o numero correspondente do remedio que gostaria de adicionar ou 0 para sair:\n')
        for idx,itens in enumerate(lista_de_remedio, start = 1):
            print(idx,'\n', itens,'\n\n')
        num = -1
        while not num in range(1,len(lista_de_remedio)): # TODO verificar se pega 0 e o ultimo numero
            num = input('Digite um numero: ').strip()
            num = ( int(num) if num.isdigit() else -1 )
        return False if num==0 else lista_de_remedio[num-1]

 # Teste ----------------------------------------------------------

teste = True
if(teste):
    nc = Carrinho_de_vendas()
    #print(nc.valor_total)
    #print(Medicamentos.lista_medicamentos)
    RemedioA=MedicFit('Coristina D',"abc",'aa','b c d e',5)
    RemedioD=MedicQuimio('Coristina E',"abc",'aa','b c d e',5,True)
    RemedioB=MedicFit('Coristina F',"abc",'aa','b c d e',50)
    RemedioC=MedicQuimio('Neosaldina',"novalgina",'aa','b c d e',15,False)
    #print(nc.localiza_remedio_por_input('Coristina'))
    #print(nc.valor_total)
    nc.editar_carrinho()