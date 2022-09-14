import redis


if __name__ == "__main__":

    redis_client = redis.Redis(
        host='localhost', port=6379
    )

    day, month, cat = 27, 12, 'اقتصادی'
    members = [title.decode() for title in redis_client.smembers(f'{day}-{month}-{cat}')]
    for title in members:
        print(title)



