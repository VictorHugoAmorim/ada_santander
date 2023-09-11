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

DIR_ESCOLAS_2 = r'arquivos csv/escolas.csv'
DIR_MATERIAL_DIDATICO_2 = r'arquivos csv/material_didatico.csv'
DIR_SUB_PREFEITURAS_2 = r'arquivos csv/subprefeituras.csv'

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
    try:
    # import
        escolas = import_csv(DIR_ESCOLAS)
        material_didatico = import_csv(DIR_MATERIAL_DIDATICO)
        sub_prefeituras = import_csv(DIR_SUB_PREFEITURAS)
    except:
        escolas = import_csv(DIR_ESCOLAS_2)
        material_didatico = import_csv(DIR_MATERIAL_DIDATICO_2)
        sub_prefeituras = import_csv(DIR_SUB_PREFEITURAS_2)
    
    # Convertendo a coluna Quantidade para o tipo númérico. Os que não puderem ser convertidos, serão NaN.
    material_didatico['quantidade'] = pd.to_numeric(material_didatico['quantidade'], errors='coerce') 
    # Alternativa 1: Substituir os NaN por 0
    # material_didatico['quantidade'].fillna(0, inplace=True) 
    # Alternativa 2: Excluir as colunas com NaN
    material_didatico.dropna(subset=['quantidade'], inplace=True)
    # Convertendo a coluna Quantidade para int
    material_didatico['quantidade'] = material_didatico['quantidade'].astype(int)
    # Para visualizar o resultado, descomentar abaixo:
    material_didatico.to_csv('mat_didatico.csv', index=False)

    # Merge
    escolas_quantidade_md = pd.merge(escolas, material_didatico, how='left', on='id')
    escolas_quantidade_md['tipo'] = escolas_quantidade_md['escolas_postos'].apply(lambda x: define_tipo(x))
    escolas_quantidade_md['id'] = escolas_quantidade_md['id'].apply(lambda x: f'{x:03d}') #Coluna id sempre com 3 dígitos
    return escolas_quantidade_md


if __name__ == '__main__':
    df = exec()
    print(df.head())
    df.to_csv('resultado.csv', index=False)