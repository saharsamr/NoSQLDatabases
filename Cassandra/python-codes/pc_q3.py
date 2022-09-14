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
    session.execute("DROP TABLE most_visited")
    session.execute("""
                      CREATE TABLE IF NOT EXISTS most_visited (
                          publish_year int,
                          vote_count int,
                          title text,
                          PRIMARY KEY ((publish_year), vote_count, title)
                       )
                       WITH CLUSTERING ORDER BY (vote_count DESC);
                    """)

    with open('../../IMDB_Dataset/title.ratings.csv', 'r') as ratings_file:
        rating_data = csv.DictReader(ratings_file, delimiter='|')
        with open('../../IMDB_Dataset/title.basics.csv', 'r') as title_basics:
            basic_data = csv.DictReader(title_basics, delimiter='|')

            for rating, basic in tqdm(zip(rating_data, basic_data)):
                if basic['startYear'] and rating['numVotes']:
                    query = """
                        INSERT INTO most_visited (publish_year, vote_count, title)
                        VALUES ({}, {}, '{}')
                        """.format(
                        int(float(basic['startYear'])), int(float(rating['numVotes'])),
                        basic['originalTitle'].replace("'", "`"))
                    session.execute(query)



