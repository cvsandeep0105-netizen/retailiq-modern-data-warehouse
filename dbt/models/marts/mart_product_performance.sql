{{ config(materialized='table') }}

with items as (
    select
        product_sk,
        count(*)::bigint as total_items_sold,
        count(distinct order_id)::bigint as total_orders,
        round(sum(item_price)::numeric, 2) as gross_item_revenue,
        round(sum(freight_value)::numeric, 2) as total_freight_value,
        round(sum(total_item_value)::numeric, 2) as total_item_value
    from {{ ref('fact_order_items') }}
    group by product_sk
)

select
    p.product_sk,
    p.product_id,
    p.product_category_name,
    p.product_category_name_english,
    p.product_weight_g,
    p.product_length_cm,
    p.product_height_cm,
    p.product_width_cm,
    coalesce(i.total_items_sold, 0) as total_items_sold,
    coalesce(i.total_orders, 0) as total_orders,
    coalesce(i.gross_item_revenue, 0) as gross_item_revenue,
    coalesce(i.total_freight_value, 0) as total_freight_value,
    coalesce(i.total_item_value, 0) as total_item_value
from {{ ref('dim_product') }} p
left join items i
    on p.product_sk = i.product_sk
