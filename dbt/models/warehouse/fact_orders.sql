with orders_base as (
    select
        row_number() over (order by order_id)::bigint as order_sk,
        order_id,
        customer_id,
        order_status,
        order_purchase_timestamp,
        order_approved_at,
        order_delivered_carrier_date,
        order_delivered_customer_date,
        order_estimated_delivery_date
    from {{ ref('int_orders') }}
)

select
    o.order_sk,
    o.order_id,
    c.customer_sk,

    purchase_date.date_sk as purchase_date_sk,
    approved_date.date_sk as approved_date_sk,
    carrier_date.date_sk as delivered_carrier_date_sk,
    delivered_date.date_sk as delivered_customer_date_sk,
    estimated_date.date_sk as estimated_delivery_date_sk,

    o.order_status,
    o.order_purchase_timestamp,
    o.order_approved_at,
    o.order_delivered_carrier_date,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,

    case
        when o.order_delivered_customer_date is not null
        then round(
            extract(
                epoch from (
                    o.order_delivered_customer_date
                    - o.order_purchase_timestamp
                )
            ) / 86400.0,
            2
        )
        else null
    end as delivery_duration_days,

    case
        when o.order_delivered_customer_date is not null
         and o.order_estimated_delivery_date is not null
        then round(
            (
                extract(
                    epoch from (
                        o.order_delivered_customer_date
                        - o.order_estimated_delivery_date::timestamp
                    )
                ) / 86400.0
                - 1
            )::numeric,
            2
        )
        else null
    end as estimated_delivery_difference_days,

    case
        when o.order_status = 'delivered'
        then true
        else false
    end as is_delivered,

    case
        when o.order_status = 'delivered'
         and o.order_delivered_customer_date is not null
         and o.order_estimated_delivery_date is not null
         and (
             extract(
                 epoch from (
                     o.order_delivered_customer_date
                     - o.order_estimated_delivery_date::timestamp
                 )
             ) / 86400.0
             - 1
         ) <= 0
        then true

        when o.order_status = 'delivered'
         and o.order_delivered_customer_date is not null
         and o.order_estimated_delivery_date is not null
        then false

        else null
    end as is_on_time,

    case
        when o.order_status = 'delivered'
         and o.order_delivered_customer_date is not null
         and o.order_estimated_delivery_date is not null
         and (
             extract(
                 epoch from (
                     o.order_delivered_customer_date
                     - o.order_estimated_delivery_date::timestamp
                 )
             ) / 86400.0
             - 1
         ) > 0
        then true

        when o.order_status = 'delivered'
         and o.order_delivered_customer_date is not null
         and o.order_estimated_delivery_date is not null
        then false

        else null
    end as is_late,

    'olist'::text as record_source,
    current_timestamp as created_at

from orders_base o

inner join {{ ref('dim_customer') }} c
    on o.customer_id = c.customer_id

left join {{ ref('dim_date') }} purchase_date
    on o.order_purchase_timestamp::date = purchase_date.calendar_date

left join {{ ref('dim_date') }} approved_date
    on o.order_approved_at::date = approved_date.calendar_date

left join {{ ref('dim_date') }} carrier_date
    on o.order_delivered_carrier_date::date = carrier_date.calendar_date

left join {{ ref('dim_date') }} delivered_date
    on o.order_delivered_customer_date::date = delivered_date.calendar_date

left join {{ ref('dim_date') }} estimated_date
    on o.order_estimated_delivery_date = estimated_date.calendar_date