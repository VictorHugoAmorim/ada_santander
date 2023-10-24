    SELECT pc."Municipio"       AS cidade,
           eb.id                AS id_estado,
           pc."Produto"         AS produto,
           pc."Data da Coleta"  AS data_coleta,
           pc."Valor de Compra" AS valor_compra,
           pc."Valor de Venda"  AS valor_revenda
      FROM public.preco_combustiveis AS pc
INNER JOIN {{ ref('estados_do_brasil') }} AS eb
        ON LOWER(pc."Estado - Sigla") = LOWER(eb.uf)