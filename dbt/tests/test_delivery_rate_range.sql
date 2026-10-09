-- Delivery-rate percentages must remain within 0-100.
select *
from {{ ref('semantic_kpis') }}
where delivery_rate_pct < 0
   or delivery_rate_pct > 100
