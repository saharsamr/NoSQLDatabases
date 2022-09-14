use hive.news;
SELECT sub_category, COUNT(*) FROM partitioned_isna WHERE main_category = ' سرویس ورزشی ' GROUP BY sub_category;