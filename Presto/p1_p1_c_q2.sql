use hive.news;
SELECT * FROM partitioned_isna WHERE text LIKE '%اوکراین%' OR summary LIKE '%اوکراین%';