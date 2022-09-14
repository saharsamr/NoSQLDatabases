use imdb;

select count(*) as count_, genre, publish_year from year_genre
where publish_year = 2020 and genre in ('Documentary', 'History', 'Reality-TV')
group by genre;
