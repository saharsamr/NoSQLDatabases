use imdb;

select genre, sum(rating)/count(*) as avg_rating from rating_tables group by genre;