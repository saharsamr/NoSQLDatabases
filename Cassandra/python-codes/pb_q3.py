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
    # session.execute("DROP TABLE Q3")
    session.execute("""
                      CREATE TABLE IF NOT EXISTS Q3 (
                          rating float,
                          rating_rank int,
                          publish_year int,
                          vote_count int,
                          title text,
                          PRIMARY KEY ((publish_year, rating_rank), vote_count)
                       )
                       WITH CLUSTERING ORDER BY (vote_count DESC);
                    """)

    with open('../../IMDB_Dataset/title.ratings.csv', 'r') as ratings_file:
        rating_data = csv.DictReader(ratings_file, delimiter='|')
        with open('../../IMDB_Dataset/title.basics.csv', 'r') as title_basics:
            basic_data = csv.DictReader(title_basics, delimiter='|')
            count = 0
            for rating, basic in tqdm(zip(rating_data, basic_data)):
                if basic['startYear'] and rating['numVotes'] and rating['averageRating']:
                    query = """
                        INSERT INTO Q3 (publish_year, vote_count, rating, rating_rank, title)
                        VALUES ({}, {}, {}, {}, '{}')
                        """.format(
                        int(float(basic['startYear'])), int(float(rating['numVotes'])),
                        float(rating['averageRating']), 1 if float(rating['averageRating']) > 7 else 0,
                        basic['originalTitle'].replace("'", "`"))
                    count += 1
                    # print(query)
                    session.execute(query)
            print(count)



