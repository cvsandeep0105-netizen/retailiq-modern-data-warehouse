{{ config(
    materialized='incremental',
    incremental_strategy='delete+insert',
    unique_key='date_sk'
) }}

with source_orders as (

    select
        fo.purchase_date_sk as date_sk,
        dd.calendar_date,
        fo.order_status,
        fo.is_delivered,
        fo.is_on_time,
        fo.is_late,
        fo.delivery_duration_days,
        fo.estimated_delivery_difference_days
    from {{ ref('fact_orders') }} fo
    inner join {{ ref('dim_date') }} dd
        on fo.purchase_date_sk = dd.date_sk

    {% if is_incremental() %}

    where dd.calendar_date >= (
        select max(dd2.calendar_date) - interval '7 days'
        from {{ ref('fact_orders') }} fo2
        inner join {{ ref('dim_date') }} dd2
            on fo2.purchase_date_sk = dd2.date_sk
    )
    and dd.calendar_date <= (
        select max(dd3.calendar_date)
        from {{ ref('fact_orders') }} fo3
        inner join {{ ref('dim_date') }} dd3
            on fo3.purchase_date_sk = dd3.date_sk
    )

    {% endif %}
)

select
    date_sk,
    count(*)::bigint as total_orders,
    count(*) filter (where is_delivered)::bigint as delivered_orders,
    count(*) filter (where order_status = 'canceled')::bigint as canceled_orders,
    count(*) filter (where order_status = 'shipped')::bigint as shipped_orders,
    count(*) filter (where order_status = 'processing')::bigint as processing_orders,
    count(*) filter (where is_on_time)::bigint as on_time_orders,
    count(*) filter (where is_late)::bigint as late_orders,
    round(avg(delivery_duration_days)::numeric, 2) as avg_delivery_duration_days,
    round(avg(estimated_delivery_difference_days)::numeric, 2) as avg_estimated_delivery_difference_days
from source_orders
group by date_sk
