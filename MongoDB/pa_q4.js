use newsdb;

db.news.updateMany(
    {},
    [
        {
            $set: {
                gregorian_date: {
                    $dateAdd : {
                        startDate : {
                            "$dateFromString" : {
                                "dateString" : {$replaceOne: {input: "$date", find: '-30', replacement: '-28'}},
                                "format" : "%Y-%m-%dT%H:%M"
                            }
                        },
                        unit : "day",
                        amount : 226899
                    }
                }
            }
        }
    ]
)jh