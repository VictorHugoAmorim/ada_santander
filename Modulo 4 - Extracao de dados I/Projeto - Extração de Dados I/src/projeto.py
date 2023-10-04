from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pandas as pd
import requests
import json
from datetime import datetime

class GetNewsApi:

    def __init__(self, from_param:str, to_param:str, api_key:str = '9a77398581d74beebbd29dbebd159a53', word_key:str = '(genômica OR genômico) AND (terapia OR sequenciamento OR doença)') -> None:
        self.api_key = api_key
        self.word_key = word_key
        self.from_param = from_param
        self.to_param = to_param
        self.spark = SparkSession.builder.appName("app").getOrCreate()

    def api_request(self):
        url = f'https://newsapi.org/v2/everything?q={self.word_key}&from_param={self.from_param}&to={self.to_param}&language=pt&sortBy=publishedAt&apiKey={self.api_key}'
        response_requests = requests.get(url).json()
        return response_requests

    def data_transform(self, json_file):
        df = self.spark.createDataFrame(pd.json_normalize(json_file['articles']))
        df = df.withColumn("publishedAt", to_timestamp(df["publishedAt"], 'yyyy-MM-dd\'T\'HH:mm:ss\'Z\''))
        df = df.na.fill("desconhecido")
        df = df.filter(col('author') != 'desconhecido')
        df = df.withColumnRenamed("source.name", "source_name")
        df = df.withColumnRenamed("source.id", "source_id")
        df.createOrReplaceTempView('df')
        return df
    
    def exec_metrics_table(self, df):
        #Tabela de métricas 1
        news_by_date = self.spark.sql(
            '''
            SELECT 
                date(publishedAt) as data_de_publicacao,
                count(*) as total_de_noticias
            FROM 
                df
            GROUP BY 
                publishedAt
            ORDER BY
                publishedAt desc
            '''
        )
        news_by_date.createOrReplaceTempView('news_by_date')
        #Tabela de métricas 2
        news_by_author = self.spark.sql(
            '''
            SELECT 
                author as autor,
                source_name as fonte,
                count(*) as total_de_noticias
            FROM 
                df
            GROUP BY 
                1,2
            '''
        )
        news_by_author.createOrReplaceTempView('news_by_author')
        #Tabela de métricas 3
        news_by_word_key = self.spark.sql(
            '''
            SELECT 
                date(publishedAt) as data_de_publicacao,
                (LEN(description) - LEN(REPLACE(lower(description), 'sequenciamento', ''))) / LEN('sequenciamento') as qtde_sequenciamento,
                (LEN(description) - LEN(REPLACE(lower(description), 'terapia', ''))) / LEN('terapia') as qtde_terapia,
                (LEN(description) - LEN(REPLACE(lower(description), 'doença', ''))) / LEN('doença') as qtde_doenca
            FROM 
                df
            '''
        )
        news_by_word_key.createOrReplaceTempView('news_by_word_key')
        return news_by_date, news_by_author, news_by_word_key

    def save_batch(self, df, news_by_date, news_by_author) -> None:
        df.write.parquet('news.parquet', mode='append')
        news_by_date.write.parquet('news_by_date.parquet', mode='append')
        news_by_author.write.parquet('news_by_author.parquet', mode='append')

    def run(self):
        json_file = self.api_request()
        df = self.data_transform(json_file)
        news_by_date, news_by_author, news_by_word_key = self.exec_metrics_table(df)
        self.save_batch(df, news_by_date, news_by_author)
        return df, news_by_date, news_by_author, news_by_word_key
    

if __name__ == '__main__':
    data_api = GetNewsApi(from_param='2023-10-01', to_param='2023-10-04')
    df, news_by_date, news_by_author, news_by_word_key  = data_api.run()
    