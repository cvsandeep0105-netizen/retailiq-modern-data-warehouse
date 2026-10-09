create index if not exists idx_mart_customer_360_customer_id
    on dbt_dev.mart_customer_360 (customer_id);

create index if not exists idx_mart_customer_360_customer_state
    on dbt_dev.mart_customer_360 (customer_state);

create index if not exists idx_mart_product_performance_product_id
    on dbt_dev.mart_product_performance (product_id);

create index if not exists idx_mart_product_performance_category
    on dbt_dev.mart_product_performance (product_category_name);

create index if not exists idx_mart_seller_performance_seller_id
    on dbt_dev.mart_seller_performance (seller_id);

create index if not exists idx_mart_daily_sales_date_sk
    on dbt_dev.mart_daily_sales (date_sk);
