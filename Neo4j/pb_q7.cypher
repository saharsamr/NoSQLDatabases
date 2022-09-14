with "
    match (b:Brand)-[h:have]->(p:Product)<-[c:contain]-(r:Receipt)<-[x:buy]-(u:User) return b.name, count(x) as customer_count order by customer_count desc;
" as query
CALL apoc.export.csv.query(query, "pb_q7.csv", {})
YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data
RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data;