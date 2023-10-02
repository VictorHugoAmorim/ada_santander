from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pandas as pd
import requests
import json

class GetNewsApi:

    def __init__(self, api_key:str = '9a77398581d74beebbd29dbebd159a53', word_key:str = 'genômica') -> None:
        self.api_key = api_key
        self.word_key = word_key
        self.spark = SparkSession.builder.appName("app").getOrCreate()

    def api_request(self):
        url = f'https://newsapi.org/v2/everything?q={self.word_key}&language=pt&sortBy=publishedAt&apiKey={self.api_key}'
        response_requests = requests.get(url).json()
        return response_requests

    def data_transform(self, json_file):
        df = self.spark.createDataFrame(pd.json_normalize(json_file['articles']))
        df = df.withColumn("publishedAt", to_timestamp(df["publishedAt"], 'yyyy-MM-dd\'T\'HH:mm:ss\'Z\''))
        df = df.na.fill("desconhecido")
        df.createOrReplaceTempView('df')
        return df
    
    def relevance_criteria(self, df):
        table = self.spark.sql(
            '''
            SELECT 
                *
            FROM 
                df
            WHERE
                author != 'desconhecido'
                AND title like '%genômica%' or  title like '%DNA%' or  title like '%doença%'
                AND description like '%genômica%' or  description like '%DNA%' and  description like '%doença%'
                AND content like '%genômica%' or  content like '%DNA%' and  content like '%doença%'
            ORDER BY
                publishedAt desc

            '''
        )
        table.createOrReplaceTempView('table')
        return table

    def save_batch(self, table) -> None:
        table.write.parquet('news.parquet', mode='overwrite')


    def run(self):
        json_file = self.api_request()
        df = self.data_transform(json_file)
        table = self.relevance_criteria(df)
        self.save_batch(table)
        return table
    

if __name__ == '__main__':
    table = GetNewsApi()
    table = table.run()
    