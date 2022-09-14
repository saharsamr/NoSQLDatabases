import redis


if __name__ == "__main__":

    redis_client = redis.Redis(
        host='localhost', port=6379
    )
    most_common = redis_client.zrange('social-tags', 0, 9, withscores=True, desc=True)
    most_common = {tag.decode(): score for (tag, score) in most_common}
    for key, value in most_common.items():
        print(key, ': ', value)




