use newsdb;

db.news.find(
    {}, {'_id': 0, 'title': 1, 'reporters': 1, 'date': 1, 'paragraph.count': 1}
).sort({'paragraph.count': -1}).limit(20)