import pandas as pd
import numpy as np
from itertools import permutations
from haversine import haversine
from matplotlib import pyplot as plt

class rotas:

    def __init__(self, dataframe):
        self.dataframe = dataframe.reset_index()
        self.qtd_escolas = len(self.dataframe)
        self.lista_index = list(self.dataframe.index)
        self._tabela_de_distancia = self.tabela_de_distancia
        self._lista_de_rotas_possiveis = self.lista_de_rotas_possiveis
        self._lista_de_distancias_por_rota = self.lista_de_distancias_por_rota
        self._melhor_rota = self.melhor_rota
        self._pior_rota = self.pior_rota
        self._dataframe_ordenada = self.dataframe_ordenada
        plt.xlabel("Latitude") 
        plt.ylabel("Longitude") 


    @property
    def tabela_de_distancia(self):
        matrix = np.zeros( ( self.qtd_escolas , self.qtd_escolas ) )
        for i,n_lin in enumerate(self.dataframe.index):
            for j,n_col in enumerate(self.dataframe.index):
                p1x = float(self.dataframe.at[n_lin,"lat"].replace(",","."))
                p1y = float(self.dataframe.at[n_lin,"lon"].replace(",","."))
                p2x = float(self.dataframe.at[n_col,"lat"].replace(",","."))
                p2y = float(self.dataframe.at[n_col,"lon"].replace(",","."))
                ponto_1 = ( (p1x,p1y) )
                ponto_2 = ( (p2x,p2y) )
                dist = haversine(ponto_1,ponto_2)
                matrix[i,j] = abs(dist)
        return matrix

    @property
    def lista_de_rotas_possiveis(self) -> list:
        perm = permutations(self.lista_index)
        return list(perm)
    
    @property
    def lista_de_distancias_por_rota(self):
        lista = list()
        for rota in self._lista_de_rotas_possiveis:
            distancia = 0
            for i in range(len(rota)-1):
                escola_a = rota[i]
                escola_b = rota[i+1]
                distancia += self._tabela_de_distancia[ escola_a , escola_b ]
            lista.append(distancia)
        return lista

    def distancia(self, qual_rota) -> list:
        index = self._lista_de_rotas_possiveis.index( qual_rota )
        return self._lista_de_distancias_por_rota[index]

    @property
    def melhor_rota(self) -> list:
        index = self._lista_de_distancias_por_rota.index( min(self._lista_de_distancias_por_rota) )
        return self._lista_de_rotas_possiveis[index]

    @property
    def pior_rota(self) -> list:
        index = self._lista_de_distancias_por_rota.index( max(self._lista_de_distancias_por_rota) )
        return self._lista_de_rotas_possiveis[index]

    def sequencia_de_coordenadas(self , rota_lista_idx:list)->list:
        lista = list()
        for idx in rota_lista_idx:
            lat = float(self.dataframe.at[idx,"lat"].replace(",","."))
            lon = float(self.dataframe.at[idx,"lon"].replace(",","."))
            coord = [ lat , lon ]
            lista.append(coord)
        return lista

    @property
    def dataframe_ordenada(self):
        dataframe_final = self.dataframe.copy()
        dataframe_final['ordem_entrega'] = ""
        for idx in self.lista_index:
            dataframe_final.at[idx,"ordem_entrega"] = str(self._melhor_rota.index(idx))
        dataframe_final = dataframe_final.sort_values("ordem_entrega")
        return dataframe_final

    def plot_rota(self,rota_lista_de_index:list=[]):
        plt.title("Coordenadas das escolas") 
        for i in self.lista_index:
            x = float(self.dataframe.at[i,"lat"].replace(",","."))
            y = float(self.dataframe.at[i,"lon"].replace(",","."))
            plt.plot( x , y ,'ro')
        if rota_lista_de_index:
            lista_coordenadas = self.sequencia_de_coordenadas(rota_lista_de_index)
            for i in range(len(lista_coordenadas)-1):
                p1 = list(lista_coordenadas[i])
                p2 = list(lista_coordenadas[i+1])

                o1 = [ p1[0] , p2[0] ]
                o2 = [ p1[1] , p2[1] ]

                plt.plot( o1 , o2 )
        return plt.show()

# teste
if (False):
    df = pd.read_csv(r'resultado.csv')
    df = df.drop((range(3,150))) # Convem reduzir o tamanho da tabela
    print('df.index')
    print(df.index)
    rota = rotas(df)
    print('dataframe')
    print(rota.dataframe)
    print('\n\n tabela_de_distancia')
    print(rota.tabela_de_distancia)
    print('\n\n lista_de_rotas_possiveis')
    print(rota.lista_de_rotas_possiveis)
    print('\n\n lista_de_distancias_por_rota')
    print(rota.lista_de_distancias_por_rota)

    # Melhor Rota
    print('\n\n melhor_rota')
    print(rota.melhor_rota)
    print('\n\n distancia')
    print(rota.distancia(rota.melhor_rota))
    print('\n\n sequencia_de_coordenadas')
    print(rota.sequencia_de_coordenadas(rota.melhor_rota))
    print('\n\n dataframe_ordenada')
    print(rota.dataframe_ordenada)
    print('\n\n plot_rota')
    rota.plot_rota(rota.melhor_rota)

    # Pior Rota
    print('\n\n pior_rota')
    print(rota.pior_rota)
    print('\n\n distancia')
    print(rota.distancia(rota.pior_rota))
    print('\n\n sequencia_de_coordenadas')
    print(rota.sequencia_de_coordenadas(rota.pior_rota))
    print('\n\n plot_rota')
    rota.plot_rota(rota.pior_rota)
