with product_base as (
    select
        row_number() over (order by product_id)::bigint as product_sk,
        product_id,
        product_category_name,
        product_name_lenght,
        product_description_lenght,
        product_photos_qty,
        product_weight_g,
        product_length_cm,
        product_height_cm,
        product_width_cm
    from {{ ref('int_products') }}
)

select
    p.product_sk,
    p.product_id,
    p.product_category_name,
    c.product_category_name_english,
    p.product_name_lenght as product_name_length,
    p.product_description_lenght as product_description_length,
    p.product_photos_qty,
    p.product_weight_g,
    p.product_length_cm,
    p.product_height_cm,
    p.product_width_cm,
    'olist'::text as record_source,
    current_timestamp as created_at
from product_base p
left join {{ ref('int_category_translation') }} c
    on p.product_category_name = c.product_category_name
