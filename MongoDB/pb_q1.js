use newsdb;

db.news.aggregate(
    [
        {
            $match: {
                text: {$regex: 'دانشگاه تهران|دانشگاه|آموزش حضوری'},
                date: {$regex: '^1400-12-25'}
            }
        },
        {
            $project: {
                _id: 0, title: 1
            }
        }
    ]
);

