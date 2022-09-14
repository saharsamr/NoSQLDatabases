use newsdb;

db.news.aggregate([
    {
        $match: {
            date: {$exists: true},
            text: {$exists: true},
            reporters: {$exists: true}
        }
    },
    {
        $project:{
            word_num: {$size: {$split: ["$text", " "]}},
            month: {$arrayElemAt: [{$split: ["$date", '-']}, 1]},
            reporters: "$reporters"
        }
    },
    {
        $group: {
            _id: {
                'month': '$month',
                'reporter': '$reporters'
            },
            total_word: {$sum: '$word_num'}
        }
    },
    {
        $sort: {'total_word': -1}
    },
    {
        $group: {
            _id: {
                month: '$_id.month',
            },
            reporters: { $push: "$_id.reporter" },
        }
    },
    {
        $project: {
            reporters: { $slice: ["$reporters", 0, 10] }
        }
    }
]);