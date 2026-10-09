{% snapshot snap_dim_customer_scd2 %}

{{
    config(
        unique_key='customer_id',
        strategy='check',
        check_cols=[
            'customer_unique_id',
            'customer_zip_code_prefix',
            'customer_city',
            'customer_state'
        ]
    )
}}

select
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state,
    'olist'::text as record_source
from {{ ref('int_customers') }}

{% endsnapshot %}
