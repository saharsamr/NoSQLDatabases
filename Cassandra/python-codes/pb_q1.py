from cassandra.cluster import Cluster

import csv
from tqdm import tqdm


if __name__ == "__main__":

    cluster = Cluster(['localhost'])
    session = cluster.connect()

    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS imdb WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}"
    )
    session.set_keyspace('imdb')
    session.execute("DROP TABLE rating_tables")
    session.execute("""
                      CREATE TABLE IF NOT EXISTS rating_tables (
                          title text,
                          genre text,
                          rating float,
                          PRIMARY KEY ((genre), rating, title)
                       )
                    """)

    with open('../../IMDB_Dataset/title.ratings.csv', 'r') as ratings_file:
        rating_data = csv.DictReader(ratings_file, delimiter='|')
        with open('../../IMDB_Dataset/title.basics.csv', 'r') as title_basics:
            basic_data = csv.DictReader(title_basics, delimiter='|')

            for rating, basic in tqdm(zip(rating_data, basic_data)):
                genres = basic['genres'].split(',')
                for genre in genres:
                    if rating['averageRating']:
                        query = """
                            INSERT INTO rating_tables (title, genre, rating)
                            VALUES ('{}', '{}', {})
                            """.format(
                            basic['originalTitle'].replace("'", "`"), genre or 'undefined', float(rating['averageRating']))
                        session.execute(query)


