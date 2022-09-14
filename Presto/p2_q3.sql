select main_category, sub_category, map(array_agg(tag), array_agg(freq))
from (
  select main_category, sub_category, tag, freq, 
    rank() over (partition by main_category, sub_category order by freq desc) rnk
    from (
      select main_category, sub_category, array_frequency(flatten(array_agg(tags))) as tag_freq
      from mongodb.newsdb.news group by main_category,sub_category)
  cross join unnest(tag_freq) as t(tag, freq)
)
where rnk < 6 group by main_category, sub_category;