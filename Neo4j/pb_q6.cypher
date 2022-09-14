with "
    match (u:User)-[b:buy]->(r:Receipt)-[con:contain]->(p:Product)-[m:member]->(c:Category)
    return
    case
    when u.age >= 20 and u.age < 35 then 'جوان'
    when u.age >= 35 and u.age < 50 then 'میانسال'
    when u.age >= 50 and u.age < 80 then 'بزرگسال'
    END As age_group,
    count(b) as count, c.name;
" as query
CALL apoc.export.csv.query(query, "pb_q6.csv", {})
YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data
RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data;