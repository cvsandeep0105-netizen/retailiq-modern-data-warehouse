-- On-time orders cannot exceed delivered orders.
select *
from {{ ref('semantic_kpis') }}
where on_time_orders > delivered_orders
