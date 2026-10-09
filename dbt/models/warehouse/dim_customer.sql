select
    row_number() over (order by customer_id)::bigint as customer_sk,
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state,
    'olist'::text as record_source,
    current_timestamp as created_at
from {{ ref('int_customers') }}
