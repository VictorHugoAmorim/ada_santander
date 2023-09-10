import csv 
import pandas as pd
import numpy as np
from datetime import datetime 
import re
from unidecode import unidecode

#Diretórios
DIR_ESCOLAS = r'..\arquivos csv\escolas.csv'
DIR_MATERIAL_DIDATICO = r'..\arquivos csv\material_didatico.csv'
DIR_SUB_PREFEITURAS = r'..\arquivos csv\subprefeituras.csv'

#Importação com tratamento de colunas
def import_csv(arq:str) -> pd.DataFrame: 
    arquivo = pd.read_csv(arq)
    # Padronizando em snake_case
    column_mapping = {col: col.strip().lower().replace(" ", "_") for col in arquivo.columns}
    arquivo.rename(columns=column_mapping, inplace=True)
    # Padronizando valores em strings em para upper case
    arquivo = arquivo.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    # Remove acentuacoes
    arquivo = arquivo.applymap(lambda x: unidecode(x) if isinstance(x, str) else x)
    return arquivo

def define_tipo(x):
    if 'EM' in x.upper() or 'E.M' in x.upper():
        return 'EM'
    elif 'CIEP' in x.upper() or 'CENTRO INTEGRADO DE EDUCAÇAO PUBLICA' in x.upper():
        return 'CIEP'
    elif 'ESCOLA' in x.upper():
        return 'ESCOLA'
    else:
        None

def exec():
    # import
    escolas = import_csv(DIR_ESCOLAS)
    material_didatico = import_csv(DIR_MATERIAL_DIDATICO)
    sub_prefeituras = import_csv(DIR_SUB_PREFEITURAS)
    # Merge
    escolas_quantidade_md = pd.merge(escolas, material_didatico, how='left', on='id')
    escolas_quantidade_md['tipo'] = escolas_quantidade_md['escolas_postos'].apply(lambda x: define_tipo(x))
    return escolas_quantidade_md


if __name__ == '__main__':
    df = exec()
    print(df.head())