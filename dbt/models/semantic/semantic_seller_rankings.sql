{{ config(materialized='view') }}

select
    seller_sk,
    seller_id,
    seller_city,
    seller_state,
    total_items_sold,
    total_orders,
    gross_item_revenue,
    total_freight_value,
    total_item_value,
    dense_rank() over (
        order by total_item_value desc
    ) as seller_revenue_rank
from {{ ref('mart_seller_performance') }}
