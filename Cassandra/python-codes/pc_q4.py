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
    session.execute("DROP TABLE genre_min")
    session.execute("""
                      CREATE TABLE IF NOT EXISTS genre_min (
                          genre text,
                          minutes int,
                          title text,
                          PRIMARY KEY ((genre), minutes, title)
                       )
                    """)

    with open('../../IMDB_Dataset/title.basics.csv', 'r') as title_basics:
        basic_data = csv.DictReader(title_basics, delimiter='|')

        for basic in tqdm(basic_data):
            genres = basic['genres'].split(',')
            for genre in genres:
                if basic['runtimeMinutes'] and genre:
                    query = """
                        INSERT INTO genre_min (minutes, genre, title)
                        VALUES ({}, '{}', '{}')
                        """.format(
                        int(float(basic['runtimeMinutes'])), genre, basic['originalTitle'].replace("'", "`")
                    )
                    session.execute(query)


