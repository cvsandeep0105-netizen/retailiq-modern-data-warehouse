with date_spine as (
    select
        generate_series(
            date '2016-01-01',
            date '2018-12-31',
            interval '1 day'
        )::date as calendar_date
)

select
    to_char(calendar_date, 'YYYYMMDD')::integer as date_sk,
    calendar_date,
    extract(year from calendar_date)::integer as calendar_year,
    extract(quarter from calendar_date)::integer as calendar_quarter,
    extract(month from calendar_date)::integer as calendar_month,
    to_char(calendar_date, 'FMMonth') as month_name,
    extract(week from calendar_date)::integer as calendar_week,
    extract(day from calendar_date)::integer as day_of_month,
    extract(isodow from calendar_date)::integer as day_of_week,
    to_char(calendar_date, 'FMDay') as day_name,
    extract(isodow from calendar_date) in (6, 7) as is_weekend
from date_spine
