select distinct (flatten(array_agg(tags))) from mongodb.newsdb.news where main_category = ' سرویس اجتماعی' or main_category = 'جامعه';
