
{{
    config(
        unique_key="id_cidade",
        on_schema_changes="sync_all_columns",
        matearialized="table"
    )
}}

WITH cidades AS (
    SELECT pc."Municipio" AS cidade,
           eb.id          AS id_estado
      FROM public.preco_combustiveis AS pc
INNER JOIN {{ ref('estados_do_brasil') }} AS eb
        ON LOWER(pc."Estado - Sigla") = LOWER(eb.uf)
  GROUP BY 1, 2
)

SELECT {{ dbt_utils.generate_surrogate_key(['cidades.cidade', 'cidades.id_estado']) }} AS id_cidade,
       cidades.cidade,
       cidades.id_estado
  FROM cidades


        