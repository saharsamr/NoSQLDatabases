use newsdb;

db.news.aggregate([
    {
        $match:{
            main_category: {$regex: 'جامعه'}
        }
    },
    {
        $out: {db: 'newsdb', coll: 'sport'}
    }
]);

db.news.deleteMany({
    main_category: {$regex: 'ورزش'}
});