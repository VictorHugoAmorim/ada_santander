import csv 
import pandas as pd
import numpy as np
from datetime import datetime 
import re

#Diretórios
DIR_ESCOLAS = r'..\arquivos csv\escolas.csv'
DIR_MATERIAL_DIDATICO = r'..\arquivos csv\material_didatico.csv'
DIR_SUB_PREFEITURAS = r'..\arquivos csv\subprefeituras.csv'

#Importação com tratamento de colunas
def import_csv(arq:str) -> pd.DataFrame: 
    arquivo = pd.read_csv(arq)
    return arquivo

def define_tipo(x):
    if 'EM' in x.upper() or 'E.M' in x.upper():
        return 'EM'
    elif 'CIEP' in x.upper() or 'CENTRO INTEGRADO DE EDUCAÇÃO PÚBLICA' in x.upper():
        return 'CIEP'
    elif 'ESCOLA' in x.upper():
        return 'ESCOLA'
    else:
        None

escolas = import_csv(DIR_ESCOLAS)
print(type(escolas))