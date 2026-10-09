{{ config(materialized='table') }}

with orders as (
    select
        customer_sk,
        count(*)::bigint as total_orders,
        count(*) filter (where is_delivered)::bigint as delivered_orders,
        count(*) filter (where is_late)::bigint as late_orders,
        round(avg(delivery_duration_days)::numeric, 2) as avg_delivery_days
    from {{ ref('fact_orders') }}
    group by customer_sk
),

items as (
    select
        customer_sk,
        count(*)::bigint as total_items,
        round(sum(total_item_value)::numeric, 2) as total_item_value
    from {{ ref('fact_order_items') }}
    group by customer_sk
),

payments as (
    select
        customer_sk,
        round(sum(payment_value)::numeric, 2) as total_payment_value
    from {{ ref('fact_payments') }}
    group by customer_sk
),

reviews as (
    select
        customer_sk,
        count(*)::bigint as total_reviews,
        round(avg(review_score)::numeric, 2) as avg_review_score
    from {{ ref('fact_reviews') }}
    group by customer_sk
)

select
    c.customer_sk,
    c.customer_id,
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    coalesce(o.total_orders, 0) as total_orders,
    coalesce(o.delivered_orders, 0) as delivered_orders,
    coalesce(o.late_orders, 0) as late_orders,
    o.avg_delivery_days,
    coalesce(i.total_items, 0) as total_items,
    coalesce(i.total_item_value, 0) as total_item_value,
    coalesce(p.total_payment_value, 0) as total_payment_value,
    coalesce(r.total_reviews, 0) as total_reviews,
    r.avg_review_score
from {{ ref('dim_customer') }} c
left join orders o on c.customer_sk = o.customer_sk
left join items i on c.customer_sk = i.customer_sk
left join payments p on c.customer_sk = p.customer_sk
left join reviews r on c.customer_sk = r.customer_sk
