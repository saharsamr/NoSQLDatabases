use imdb;

capture 'temp.csv';
select genre, avg(minutes) as avg_minutes from genre_min group by genre;
capture off;

create table sort_avg (aim text, avg_min int, genre text, primary key ((aim), avg_min, genre));
copy sort_avg (aim, genre, avg_min) from 'temp.csv' with header=true;
select genre, avg_min from sort_avg;
