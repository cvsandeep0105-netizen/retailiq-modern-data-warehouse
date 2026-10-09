with order_items_base as (
    select
        row_number() over (
            order by order_id, order_item_id
        )::bigint as order_item_sk,
        order_id,
        order_item_id,
        product_id,
        seller_id,
        shipping_limit_date,
        price,
        freight_value
    from {{ ref('int_order_items') }}
)

select
    oi.order_item_sk,
    oi.order_id,
    oi.order_item_id,

    c.customer_sk,
    p.product_sk,
    s.seller_sk,

    d.date_sk as order_date_sk,

    oi.shipping_limit_date,

    oi.price::numeric as item_price,
    oi.freight_value::numeric as freight_value,

    round(
        (
            oi.price::numeric
            + oi.freight_value::numeric
        ),
        2
    ) as total_item_value,

    'olist'::text as record_source,
    current_timestamp as created_at

from order_items_base oi

inner join {{ ref('int_orders') }} o
    on oi.order_id = o.order_id

inner join {{ ref('dim_customer') }} c
    on o.customer_id = c.customer_id

inner join {{ ref('dim_product') }} p
    on oi.product_id = p.product_id

inner join {{ ref('dim_seller') }} s
    on oi.seller_id = s.seller_id

inner join {{ ref('dim_date') }} d
    on o.order_purchase_timestamp::date = d.calendar_date