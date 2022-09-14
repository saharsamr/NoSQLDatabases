USE imdb;

CREATE EXTERNAL TABLE title_basics(
	tconst STRING, title_type STRING, primary_title STRING, 
	original_title STRING, is_adult INT, start_year STRING, 
	end_year STRING, runtime_minutes INT, 
	genres STRING
)
COMMENT 'title-basics'
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION '/data/imdb-title-basics'
TBLPROPERTIES("skip.header.line.count"="1");

LOAD DATA INPATH '/data/title-basics' INTO TABLE title_basics;


CREATE EXTERNAL TABLE title_crew(
	tconst STRING, directors ARRAY<STRING>, writers ARRAY<STRING>
)
COMMENT 'title-crew'
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION '/data/imdb-title-crew'
TBLPROPERTIES("skip.header.line.count"="1");

LOAD DATA INPATH '/data/title-crew' INTO TABLE title_crew;


CREATE EXTERNAL TABLE title_ratings(
	tconst STRING, average_rating FLOAT, num_votes INT
)
COMMENT 'title-ratings'
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION '/data/imdb-title-ratings'
TBLPROPERTIES("skip.header.line.count"="1");

LOAD DATA INPATH '/data/title-ratings' INTO TABLE title_ratings;


SELECT * FROM title_ratings;
SELECT * FROM title_crew;
SELECT * FROM title_basics;

SHOW TABLES IN imdb;
