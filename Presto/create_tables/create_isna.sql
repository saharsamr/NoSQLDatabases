USE news;

CREATE EXTERNAL TABLE isna(
	code BIGINT, title STRING, date_ STRING, 
	text STRING, summary STRING, tags STRING, 
	main_category STRING, sub_category STRING, 
	short_link STRING
)
COMMENT 'isna data'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/data/news/isna'
TBLPROPERTIES("skip.header.line.count"="1");

LOAD DATA INPATH '/data/news/isna.csv' INTO TABLE isna;

SELECT * FROM isna;

SHOW TABLES IN news;
