{{ config(materialized='table') }}

select
    date_sk,
    total_orders,
    delivered_orders,
    canceled_orders,
    shipped_orders,
    processing_orders,
    on_time_orders,
    late_orders,
    avg_delivery_duration_days,
    avg_estimated_delivery_difference_days
from {{ ref('fct_daily_order_metrics') }}
