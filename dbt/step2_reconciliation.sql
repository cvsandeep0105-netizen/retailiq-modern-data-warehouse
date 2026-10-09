select
    'FACT_ORDERS' as layer,
    count(*)::bigint as row_count
from dbt_dev.fact_orders

union all

select
    'DAILY_INCREMENTAL',
    sum(total_orders)::bigint
from dbt_dev.fct_daily_order_metrics

union all

select
    'DAILY_MART',
    sum(total_orders)::bigint
from dbt_dev.mart_daily_sales

union all

select
    'CUSTOMER_MART',
    sum(total_orders)::bigint
from dbt_dev.mart_customer_360

union all

select
    'FACT_ORDER_ITEMS',
    count(*)::bigint
from dbt_dev.fact_order_items

union all

select
    'PRODUCT_MART_ITEMS',
    sum(total_items_sold)::bigint
from dbt_dev.mart_product_performance

union all

select
    'SELLER_MART_ITEMS',
    sum(total_items_sold)::bigint
from dbt_dev.mart_seller_performance

union all

select
    'FACT_REVIEWS',
    count(*)::bigint
from dbt_dev.fact_reviews

union all

select
    'REVIEW_MART_REVIEWS',
    sum(review_count)::bigint
from dbt_dev.mart_review_performance

order by layer;
