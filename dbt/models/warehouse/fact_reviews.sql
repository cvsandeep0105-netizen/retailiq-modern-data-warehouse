with reviews_base as (
    select
        row_number() over (
            order by order_id, review_id
        )::bigint as review_sk,
        review_id,
        order_id,
        review_score,
        review_comment_title,
        review_comment_message,
        review_creation_date,
        review_answer_timestamp
    from {{ ref('int_order_reviews') }}
)

select
    r.review_sk,
    r.review_id,
    r.order_id,
    c.customer_sk,
    r.review_score,
    r.review_comment_title,
    r.review_comment_message,
    r.review_creation_date as review_creation_timestamp,
    r.review_answer_timestamp,
    d.date_sk as review_creation_date_sk,
    'olist'::text as record_source,
    current_timestamp as created_at
from reviews_base r
inner join {{ ref('int_orders') }} o
    on r.order_id = o.order_id
inner join {{ ref('dim_customer') }} c
    on o.customer_id = c.customer_id
left join {{ ref('dim_date') }} d
    on r.review_creation_date::date = d.calendar_date
