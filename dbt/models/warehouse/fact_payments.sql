with payments_base as (

    select
        row_number() over (
            order by order_id, payment_sequential
        )::bigint as payment_sk,
        order_id,
        payment_sequential,
        payment_type,
        payment_installments,
        payment_value
    from {{ ref('int_order_payments') }}

)

select
    p.payment_sk,
    p.order_id,
    p.payment_sequential,
    c.customer_sk,
    p.payment_type,
    p.payment_installments,
    p.payment_value::numeric as payment_value,
    d.date_sk as payment_date_sk,
    'olist'::text as record_source,
    current_timestamp as created_at

from payments_base p

inner join {{ ref('int_orders') }} o
    on p.order_id = o.order_id

inner join {{ ref('dim_customer') }} c
    on o.customer_id = c.customer_id

inner join {{ ref('dim_date') }} d
    on o.order_purchase_timestamp::date = d.calendar_date