import csv 
import pandas as pd
import numpy as np
from datetime import datetime 

#Diretórios
DIR_ESCOLAS = r'..\arquivos csv\escolas.csv'
DIR_MATERIAL_DIDATICO = r'..\arquivos csv\material_didatico.csv'
DIR_SUB_PREFEITURAS = r'..\arquivos csv\subprefeituras.csv'

def import_csv(arq:str) -> pd.DataFrame: 
    arquivo = pd.read_csv(arq)
    return arquivo


escolas = import_csv(DIR_ESCOLAS)
print(type(escolas))