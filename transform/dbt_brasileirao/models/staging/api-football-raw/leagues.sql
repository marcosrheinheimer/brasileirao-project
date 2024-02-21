with orders as (

    select
        *
    from {{ source('api-football-raw', 'leagues')}}

)

select * from orders