use imdb;

select title, publish_year, vote_count from most_visited where publish_year IN (2020, 2021) per partition limit 10;

