use newsdb;

db.news.aggregate([
    {
        $match: {date: {$exists: true}}
    },
    {
        $project: {
            time: {$arrayElemAt: [{$split: ["$date", "T"]}, 1]}
        }
    },
    {
        $project: {
            hour: {
                $toInt: {
                    $divide: [{$toInt: {$arrayElemAt: [{$split: ["$time", ":"]}, 0]}}, 6]
                }
            }
        }
    },
    {
        $group: {
            _id: '$hour',
            count: {$sum: 1}
        }
    }
]);