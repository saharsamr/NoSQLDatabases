USE news;

CREATE EXTERNAL TABLE partitioned_isna(
	code BIGINT, title STRING, date_ STRING, 
	text STRING, summary STRING, tags STRING, 
	sub_category STRING, short_link STRING
)
PARTITIONED BY (main_category STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/data/news/isna'
TBLPROPERTIES("skip.header.line.count"="1");

SET hive.exec.dynamic.partition.mode=nonstrict

INSERT OVERWRITE TABLE partitioned_isna PARTITION(main_category) 
SELECT code, title, date_, text, summary, tags, sub_category, short_link, main_category FROM isna;

SELECT * FROM partitioned_isna;

SHOW TABLES IN news;
