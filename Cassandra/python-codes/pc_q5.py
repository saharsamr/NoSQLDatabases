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
    session.execute("DROP TABLE year_genre")
    session.execute("""
                      CREATE TABLE IF NOT EXISTS year_genre (
                          publish_year int,
                          genre text,
                          title text,
                          PRIMARY KEY ((publish_year, genre), title)
                       )
                    """)

    with open('../../IMDB_Dataset/title.basics.csv', 'r') as title_basics:
        basic_data = csv.DictReader(title_basics, delimiter='|')

        for basic in tqdm(basic_data):
            genres = basic['genres'].split(',')
            for genre in genres:
                if basic['startYear']:
                    # if genre == 'Documentary' and int(float(basic['startYear'])) == 2020:
                    #     print('found')
                    query = """
                        INSERT INTO year_genre (publish_year, genre, title)
                        VALUES ({}, '{}', '{}')
                        """.format(
                        int(float(basic['startYear'])), genre, basic['originalTitle'].replace("'", "`")
                    )
                    session.execute(query)


