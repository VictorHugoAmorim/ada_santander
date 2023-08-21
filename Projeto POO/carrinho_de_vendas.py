from medicamentos import Medicamentos
from medic_fit import MedicFit
from medic_quimio import MedicQuimio
from functools import reduce

# by NWErickSasaki

class Carrinho_de_vendas:

    def __init__(self, carrinho:list=[[],[]]):
        self.carrinho = carrinho # [ [obj_Med_A , obj_Med_B , ... ] , [ 1 , 3 , ... ] ]
        self._valor_total = self.valor_total

    def __repr__(self) -> str: # TODO
        txt =  """
        \t-------------------------- COMPRA --------------------------\n
        \tID\tMEDICAMENTO\tQTD\tPREÇO\t\tSUB-TOTAL\n\n"""
        for idx,itens in enumerate(self.carrinho[0], start=1):
            txt += f"\t\t{idx}\t{itens.nome.upper()}\t{str(self.carrinho[1][idx-1])}\tR$ {itens.valor:.2f}\tR$ {itens.valor*self.carrinho[1][idx-1]:.2f}   \n"
        txt += f"\n\t\tTOTAL \t\tR$ {self.valor_total:.2f}"
        return txt

    @property
    def valor_total(self) -> float:
        lista_em_duplas = [] # [ [rem,1] , [rem_A,3] ... ]
        for i in range (len(self.carrinho[0])):
            lista_em_duplas.append([self.carrinho[0][i],self.carrinho[1][i]])
        soma = lambda element , inicio : element + inicio
        self._valor_total = reduce(soma, ( itens[0].valor * itens[1] for itens in lista_em_duplas) , 0)
        return self._valor_total

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
                    remedio_selecionado=self.localiza_remedio_por_input()
                    if self.medicamento_ja_no_carrinho(remedio_selecionado):
                        self.altera_no_carrinho_a_quantidade_do(remedio_selecionado)
                        continue
                    elif self.verifica_se_precisa_de_receita(remedio_selecionado):
                        if not self.cliente_tem_receita_para(remedio_selecionado):
                            print(f'Nao adicionado ao carrinho: {remedio_selecionado.nome}')
                            continue
                    quantidade = self.pede_input_de_quantidade_desejada_de(remedio_selecionado)
                    self.adiciona_no_carrinho(remedio_selecionado, quantidade)
        
                case '3':
                    remedio_selecionado = self.localiza_remedio_por_input(onde=self.carrinho[0])
                    self.altera_no_carrinho_a_quantidade_do(remedio_selecionado)

                case '4':
                    remedio_selecionado = self.localiza_remedio_por_input(onde=self.carrinho[0])
                    self.retirar_do_carrinho(remedio_selecionado) 

                case '0':
                    return self

                case _:
                    print(f"A opcao '{opcao}' é invalida!")

    def altera_no_carrinho_a_quantidade_do(self, remedio_selecionado:Medicamentos, nova_quantidade:int=0) -> None:
        nova_quantidade = (self.pede_input_de_quantidade_desejada_de(remedio_selecionado) if nova_quantidade==0 else nova_quantidade)
        if nova_quantidade <= 0:
            self.retirar_do_carrinho(remedio_selecionado)
        elif remedio_selecionado in self.carrinho[0]:
            idx = self.carrinho[0].index(remedio_selecionado)
            self.carrinho[1][idx] = nova_quantidade
            print(f'Alterado para: {nova_quantidade} x {remedio_selecionado.nome}')
        else:
            self.adiciona_no_carrinho(remedio_selecionado, nova_quantidade)
        return None


    def cliente_tem_receita_para(self, remedio_selecionado:Medicamentos) -> bool:
        num = input(f"""
        O Cliente tem receita para
        "{remedio_selecionado.nome}"?

        1 - Sim
        2 - Não
        * - Voltar
        
        Digite o numero correspondente: """).strip()
        return (True if num == "1" else False)

    def verifica_se_precisa_de_receita(self, remedio:Medicamentos)-> bool:
        if isinstance(remedio, MedicQuimio):
            return remedio.necessita_receita
        return False

    def medicamento_ja_no_carrinho(self, remedio_selecionado:Medicamentos) -> bool:
        if remedio_selecionado in self.carrinho[0]:
            return True
        elif not remedio_selecionado in self.carrinho[0]:
            return False
        else:
            raise ValueError

    def pede_input_de_quantidade_desejada_de(self, remedio_selecionado:Medicamentos) -> int:
        num = -1
        while num != 0:
            num = input(f'Digite a quantidade deseja de "{remedio_selecionado.nome}" que gostaria de ter no carrinho: ').strip()
            if num.isdigit():
                num = int(num)
                return num

    def adiciona_no_carrinho(self, remedio_selecionado:Medicamentos, quantidade:int=1) -> None:
        if quantidade:
            self.carrinho[0].append(remedio_selecionado)
            self.carrinho[1].append(quantidade)
            print(f'Adicionado: {quantidade} x "{remedio_selecionado.nome}"')
            return None
        print(f"Nao foi adicionado ao carrinho: {remedio_selecionado}")

    def retirar_do_carrinho(self, remedio_selecionado:Medicamentos) -> Medicamentos:
        if remedio_selecionado in self.carrinho[0]:
            idx = self.carrinho[0].index(remedio_selecionado)
            self.carrinho[0].pop(idx)
            self.carrinho[1].pop(idx)
            print(f'Retirado do carrinho: {remedio_selecionado.nome}')
        return remedio_selecionado

    def localiza_remedio_por_input( self , palavra_do_remedio:str="" , onde:list=Medicamentos.lista_medicamentos ) -> Medicamentos:
        if not palavra_do_remedio:
            palavra_do_remedio =  input('Digite qual remedio está procurando:')
        palavra_do_remedio = palavra_do_remedio.lower()

        lista_remedios_por_nome = [ remedio for remedio in onde if palavra_do_remedio in remedio.nome.lower()]
        lista_remedios_por_principal_composto = [ remedio for remedio in onde if palavra_do_remedio in remedio.principal_composto.lower()]
        lista_remedios_por_descricao = [ remedio for remedio in onde if palavra_do_remedio in remedio.descricao.lower()]
        lista_remedios_por_laboratorio = [ remedio for remedio in onde if palavra_do_remedio in remedio.laboratorio.nome.lower()]
        lista_todos = lista_remedios_por_nome + lista_remedios_por_principal_composto + lista_remedios_por_laboratorio + lista_remedios_por_descricao
        
        dict_remedios={}
        for e in lista_todos:
            dict_remedios[e] = e
        lista_de_remedio = list(dict_remedios)

        if not lista_de_remedio:
            print('Medicamento nao encontrado!! :(')
            self.localiza_remedio_por_input("", onde)
        elif len(lista_de_remedio)>1:
            return self.escolha_um_remedio_na(lista_de_remedio)
        else:
            return lista_de_remedio[0]  ### TODO da pra otimizar porem quando a lista só tem index 0 quebra

    def escolha_um_remedio_na(self, lista_de_remedio: list) -> Medicamentos:
        print('Digite o numero correspondente do remedio que gostaria de adicionar ou 0 para sair:\n')
        for idx,itens in enumerate(lista_de_remedio, start = 1):
            print(idx, itens,'\n')
        num = -1
        while not num in range(1,len(lista_de_remedio)+1):
            num = input('Digite um numero: ').strip()
            num = ( int(num) if num.isdigit() else -1 )
        return False if num==0 else lista_de_remedio[num-1]

    def remedio_mais_vendido_do_carrinho_e_quanto(lista:list) -> (Medicamentos, int):
        quantidade = max(lista[1])
        remedio_mais_vendido = lista[0].index(quantidade)
        return (remedio_mais_vendido, quantidade)


# Teste ----------------------------------------------------------

TESTE = 0
if TESTE:
    print('\n\n VOCE ESTA RODANDO UM TESTE \n\n')
    from lendocsv import lendo_csv
    lendo_csv()
    nc = Carrinho_de_vendas()
    nc.editar_carrinho()

    # erro ao puxar carrinho [,[0,2]]