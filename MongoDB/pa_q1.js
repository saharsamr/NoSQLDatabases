use newsdb;

db.news.aggregate(
    [
        {
            $match: {main_category: {$in: ['سرویس اجتماعی', 'جامعه']}}
        },
        {
            $unwind: "$tags"
        },
        {
            $group: {
                _id: null,
                tags_s: {
                    $addToSet: "$tags"
                }
            }
        }
    ]
);