{{ config(materialized='view') }}

select
    sum(total_orders)::bigint as total_orders,
    sum(delivered_orders)::bigint as delivered_orders,
    sum(canceled_orders)::bigint as canceled_orders,
    sum(shipped_orders)::bigint as shipped_orders,
    sum(processing_orders)::bigint as processing_orders,
    sum(on_time_orders)::bigint as on_time_orders,
    sum(late_orders)::bigint as late_orders,
    round(
        100.0 * sum(delivered_orders) / nullif(sum(total_orders), 0),
        2
    ) as delivery_rate_pct,
    round(
        100.0 * sum(on_time_orders) / nullif(sum(delivered_orders), 0),
        2
    ) as on_time_rate_pct,
    round(
        100.0 * sum(late_orders) / nullif(sum(delivered_orders), 0),
        2
    ) as late_rate_pct,
    round(avg(avg_delivery_duration_days), 2) as avg_delivery_duration_days,
    round(avg(avg_estimated_delivery_difference_days), 2) as avg_estimated_delivery_difference_days
from {{ ref('mart_daily_sales') }}
