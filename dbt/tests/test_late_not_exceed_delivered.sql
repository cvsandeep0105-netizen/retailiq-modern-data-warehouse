-- Late orders cannot exceed delivered orders.
select *
from {{ ref('semantic_kpis') }}
where late_orders > delivered_orders
