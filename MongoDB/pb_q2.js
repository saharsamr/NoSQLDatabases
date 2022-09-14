use newsdb;

db.news.aggregate([
    { $unwind: "$tags" },
    {
        $group: {
            "_id": { tag: "$tags", m: "$main-category", s: "$sub-category" },
            "count": { $sum: 1 },
        }
    },
    { $sort: { "count": -1 } },
    {
        $group: {
            "_id": { m: "$_id.m", s: "$_id.s" },
            tags: { $push: "$_id.tag" }
        }
    },
    {
        $project: {
            tags: { $slice: ["$tags", 0, 5] }
        }
    }
]);