import redis


if __name__ == "__main__":

    redis_client = redis.Redis(
        host='localhost', port=6379
    )
    month = 12
    week_keys = [f'{day}-{month}' for day in range(21, 28)]
    count = 0
    for key in week_keys:
        count += redis_client.llen(key)

    print('number of published news in week 21-27 Esfand: ', count)



