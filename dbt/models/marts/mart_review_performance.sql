{{ config(materialized='table') }}

select
    review_score,
    count(*)::bigint as review_count,
    round(avg(review_score)::numeric, 2) as average_score,
    count(*) filter (
        where review_comment_message is not null
          and trim(review_comment_message) <> ''
    )::bigint as reviews_with_comments,
    count(*) filter (
        where review_answer_timestamp is not null
    )::bigint as reviews_answered
from {{ ref('fact_reviews') }}
group by review_score
order by review_score
