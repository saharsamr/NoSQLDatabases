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
    session.execute("DROP TABLE directors_table2")
    session.execute("""
                      CREATE TABLE IF NOT EXISTS directors_table2 (
                          writer text,
                          director text,
                          title text,
                          genre text,
                          PRIMARY KEY ((genre), title)
                       )
                    """)

    name_mapping = {}
    with open('../../IMDB_Dataset/name.basics.csv', 'r') as name_file:
        name_data = csv.DictReader(name_file, delimiter='|')
        for name_record in name_data:
            name_mapping[name_record['nconst']] = name_record['primaryName']

    with open('../../IMDB_Dataset/title.basics.csv', 'r') as basics_file:
        basics_data = csv.DictReader(basics_file, delimiter='|')
        with open('../../IMDB_Dataset/title.crew.csv', 'r') as crew_file:
            crew_data = csv.DictReader(crew_file, delimiter='|')

            for basic, crew in tqdm(zip(basics_data, crew_data)):
                directors = '-'.join([name_mapping[director_id] for director_id in crew['directors'].split(',')])
                writers = '-'.join([name_mapping[writer_id] for writer_id in crew['writers'].split(',')])
                genres = basic['genres'].split(',')
                if genres:
                    for genre in genres:
                        query = """
                            INSERT INTO directors_table2 (writer, director, title, genre)
                            VALUES ('{}', '{}', '{}', '{}')
                            """.format(
                            writers.replace("'", "`") or 'undefined',
                            directors.replace("'", "`") or 'undefined',
                            basic['originalTitle'].replace("'", "`"), genre or 'undefined')

                        session.execute(query)



