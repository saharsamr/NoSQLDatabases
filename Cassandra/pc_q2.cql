use imdb;

select count(*), director from dir_pub where publish_year > 2020 group by director ALLOW FILTERING;