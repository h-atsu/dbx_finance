{ { config(materialized = 'view') } } with source_data as (
    select *
    from { { source('raw', 'stock_prices') } }
)
select ticker,
    date,
    open,
    high,
    low,
    close,
    volume,
    _ingested_at
from source_data