use newsdb;

db.news.updateMany(
    {
        editors: {$exists: true},
        reporters: {$exists: false}
    },
    {
        $unset: {'reporter-code': 1}
    }
);
