USE hive.imdb;

SELECT c.directors, c.writers
FROM ((SELECT tconst FROM title_basics WHERE original_title = 'The Godfather') as b 
JOIN (SELECT tconst, directors, writers FROM title_crew) as c
ON (b.tconst = c.tconst));