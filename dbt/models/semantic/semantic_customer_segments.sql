{{ config(materialized='view') }}

select
    customer_sk,
    customer_id,
    customer_city,
    customer_state,
    total_orders,
    total_items,
    total_item_value,
    total_payment_value,
    total_reviews,
    avg_review_score,
    case
        when total_orders >= 5 then 'High Value'
        when total_orders >= 2 then 'Repeat'
        else 'Single Order'
    end as customer_order_segment
from {{ ref('mart_customer_360') }}
