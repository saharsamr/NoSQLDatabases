match (u:User)-[r:buy]->() Return u, count(r) as order_count order by order_count desc limit 1;

match (u:User)-->(r:Receipt) Return u, sum(r.amount) as amount order by amount desc limit 1;