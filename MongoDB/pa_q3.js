use newsdb;

db.news.updateMany(
    {
        text: {$exists: true}
    },
    [
        {"$set": {"paragraph": {"count": {$size: {$split: ["$text", "#"]}}}}}
    ]
);