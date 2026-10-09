\timing on

select
    'mart_customer_360' as model,
    count(*) as rows
from dbt_dev.mart_customer_360;

select
    'mart_product_performance' as model,
    count(*) as rows
from dbt_dev.mart_product_performance;

select
    'mart_seller_performance' as model,
    count(*) as rows
from dbt_dev.mart_seller_performance;

select
    'mart_review_performance' as model,
    count(*) as rows
from dbt_dev.mart_review_performance;

select
    'mart_daily_sales' as model,
    count(*) as rows
from dbt_dev.mart_daily_sales;

explain (analyze, buffers)
select *
from dbt_dev.mart_customer_360
limit 100;

explain (analyze, buffers)
select *
from dbt_dev.mart_product_performance
limit 100;

explain (analyze, buffers)
select *
from dbt_dev.mart_seller_performance
limit 100;
