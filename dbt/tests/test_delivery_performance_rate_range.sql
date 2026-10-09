-- On-time and late percentages must remain within 0-100.
select *
from {{ ref('semantic_kpis') }}
where on_time_rate_pct < 0
   or on_time_rate_pct > 100
   or late_rate_pct < 0
   or late_rate_pct > 100
