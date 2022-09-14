import json
import redis


def write_data_in_redis(json_file):

    with open(json_file, 'r') as f:
        data = json.loads(f.read())

    redis_client = redis.Redis(
        host='localhost', port=6379
    )

    for row in data:

        if row.get('main_category') and ('ورزشی' in row.get('main_category')):

            reporter = row.get('reporters')
            reporter_code = row.get('reporter_codes;')
            if reporter and reporter_code:
                redis_client.hset('reporter-code-mapping', mapping={reporter: reporter_code})
            if reporter:
                redis_client.sadd('reporters', reporter)
            if reporter_code:
                redis_client.sadd('reporter-codes', reporter_code)

        if row.get('main_category') and ('اجتماعی' in row.get('main_category') or 'جامعه' in row.get('main_category')):

            tags = row.get('tags')
            for tag in tags:
                redis_client.zincrby('social-tags', 1, tag)

        # from 21 to 27 in Esfand 1400
        date = row.get('date').split('T')[0]
        date = date.split('-')
        day, month = date[2], date[1]
        redis_client.lpush(f'{day}-{month}', row.get('code'))
        if row.get('main_category') and ('اقتصاد' in row.get('main_category')):
            cat = 'اقتصادی'
            redis_client.sadd(f'{day}-{month}-{cat}', row.get('title'))


if __name__ == "__main__":

    write_data_in_redis('data.json')
