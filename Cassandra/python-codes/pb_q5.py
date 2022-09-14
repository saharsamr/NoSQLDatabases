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
    session.execute("DROP TABLE Q5")
    session.execute("""
                      CREATE TABLE IF NOT EXISTS Q5 (
                          publish_year int,
                          tconst text,
                          PRIMARY KEY (publish_year, tconst)
                       )
                    """)

    with open('../../IMDB_Dataset/title.basics.csv', 'r') as title_basics:
        basic_data = csv.DictReader(title_basics, delimiter='|')

        for basic in tqdm(basic_data):
            if basic['startYear']:
                query = """
                    INSERT INTO Q5 (publish_year, tconst)
                    VALUES ({}, '{}')
                    """.format(
                    int(float(basic['startYear'])), basic['tconst'])

                session.execute(query)





