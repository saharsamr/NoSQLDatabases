use hive.news;
SELECT sub_category, COUNT(*) FROM isna WHERE main_category = ' سرویس ورزشی ' GROUP BY sub_category;