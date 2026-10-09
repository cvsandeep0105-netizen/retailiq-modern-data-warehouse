select
    row_number() over (order by seller_id)::bigint as seller_sk,
    seller_id,
    seller_zip_code_prefix,
    seller_city,
    seller_state,
    'olist'::text as record_source,
    current_timestamp as created_at
from {{ ref('int_sellers') }}
