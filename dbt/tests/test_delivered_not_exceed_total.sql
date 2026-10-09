-- Delivered orders cannot exceed total orders.
select *
from {{ ref('semantic_kpis') }}
where delivered_orders > total_orders
