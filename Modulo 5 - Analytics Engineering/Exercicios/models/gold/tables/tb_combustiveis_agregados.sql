{{
  config(
    materialized="table"
  )
}}

  SELECT {{ dbt_utils.generate_surrogate_key(['municipio', 'sigla_estado']) }} as id,
         ref.municipio,
         ref.sigla_estado,
         round(AVG(ref.valor_de_venda), 2) AS media
    FROM {{ ref('tb_precos_combustiveis_refinado') }} ref
   WHERE ref.municipio IN ('SAO PAULO', 'GOIANIA', 'FORTALEZA')
GROUP BY ref.municipio, ref.sigla_estado