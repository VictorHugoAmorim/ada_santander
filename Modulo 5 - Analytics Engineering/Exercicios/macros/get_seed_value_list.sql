{% macro get_seed_list(table_name, values_column) %}
    SELECT {{ values_column }}
      FROM {{ table_name }}
{% endmacro %}