
{{
    config(
        matarialized="view"
    )
}}

SELECT {{ dbt_utils.generate_surrogate_key(['"Municipio"', '"Produto"', '"Valor de Venda"', "'Data da Coleta'"]) }} AS id_registro,
       pc."Municipio"                                        AS cidade,
       pc."Produto"                                          AS produto,
       CAST(REPLACE(pc."Valor de Venda", ',', '.') AS FLOAT) AS valor_revenda,
       pc."Data da Coleta"                                   AS data_coleta
  FROM public.preco_combustiveis pc