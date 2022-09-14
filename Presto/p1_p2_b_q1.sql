USE hive.imdb;

SELECT b.original_title, r.average_rating 
FROM ((SELECT original_title, tconst, title_type FROM title_basics WHERE title_type = 'movie' AND start_year = '2021') as b 
JOIN (SELECT tconst, average_rating FROM title_ratings WHERE average_rating > 9.0) as r
ON (b.tconst = r.tconst)) ORDER BY r.average_rating DESC LIMIT 10;