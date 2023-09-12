import pandas as pd
import numpy as np
from itertools import permutations
from haversine import haversine

class melhor_rota:

    def __init__(self, dataframe):
        self.dataframe = dataframe.reset_index()
        self.qtd_escolas = len(self.dataframe)
        self.lista_index = list(self.dataframe.index)
        self._tabela_de_distancia = self.tabela_de_distancia
        self._lista_de_rotas_possiveis = self.lista_de_rotas_possiveis
        self._lista_de_distancias_por_rota = self.lista_de_distancias_por_rota
        self._menor_distancia = self.menor_distancia
        self._melhor_rota = self.melhor_rota
        self._sequencia_de_coordenadas = self.sequencia_de_coordenadas
        self._dataframe_ordenada = self.dataframe_ordenada
        #TODO imagem plot do percurso

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

    @property
    def menor_distancia(self) -> list:
        return min(self._lista_de_distancias_por_rota)

    @property
    def melhor_rota(self) -> list:
        index = self._lista_de_distancias_por_rota.index( self._menor_distancia )
        return self._lista_de_rotas_possiveis[index]

    @property
    def sequencia_de_coordenadas(self)->list:
        lista = list()
        for idx in self._melhor_rota:
            lat = float(self.dataframe.at[idx,"lat"].replace(",","."))
            lon = float(self.dataframe.at[idx,"lon"].replace(",","."))
            coord = ( (lat,lon) )
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


# teste
if (False):
    df = pd.read_csv(r'resultado.csv')
    df = df.drop((range(3,150)))
    print('df.index')
    print(df.index)
    rotas = melhor_rota(df)
    print('dataframe')
    print(rotas.dataframe)
    print('\n\n tabela_de_distancia')
    print(rotas.tabela_de_distancia)
    print('\n\n lista_de_rotas_possiveis')
    print(rotas.lista_de_rotas_possiveis)
    print('\n\n lista_de_distancias_por_rota')
    print(rotas.lista_de_distancias_por_rota)
    print('\n\n melhor_rota')
    print(rotas.melhor_rota)
    print('\n\n menor_distancia')
    print(rotas.menor_distancia)
    print('\n\n sequencia_de_coordenadas')
    print(rotas.sequencia_de_coordenadas)
    print('\n\n dataframe_ordenada')
    print(rotas.dataframe_ordenada)

