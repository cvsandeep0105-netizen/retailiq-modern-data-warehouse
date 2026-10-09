{{ config(materialized='view') }}

select
    product_category_name_english,
    count(*)::bigint as product_count,
    sum(total_items_sold)::bigint as total_items_sold,
    sum(total_orders)::bigint as total_orders,
    round(sum(gross_item_revenue)::numeric, 2) as gross_item_revenue,
    round(sum(total_freight_value)::numeric, 2) as total_freight_value,
    round(sum(total_item_value)::numeric, 2) as total_item_value
from {{ ref('mart_product_performance') }}
group by product_category_name_english
