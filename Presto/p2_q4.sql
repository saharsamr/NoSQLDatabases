select count(*) from (
  select floor(cast(regexp_replace(regexp_extract(news.date, 'T\d+:'), 'T|:')
  as integer)/6) as day_time from mongodb.newsdb.news as news)
group by day_time;