SELECT pc."Municipio"                                        AS municipio,
       pc."Estado - Sigla"                                   AS sigla_estado,
       CAST(REPLACE(pc."Valor de Venda", ',', '.') AS NUMERIC) AS valor_de_venda
  FROM public.preco_combustiveis AS pc