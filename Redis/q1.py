import redis


if __name__ == "__main__":

    redis_client = redis.Redis(
        host='localhost', port=6379
    )
    reporters = [reporter.decode() for reporter in redis_client.smembers('reporters')]
    reporter_codes = [code.decode() for code in redis_client.smembers('reporter-codes')]
    common_count = redis_client.hlen('reporter-code-mapping')

    print('reporters-list:')
    for reporter in reporters:
        print(reporter)
    print('reporter-codes:')
    print(reporter_codes)
    print('num of reporters:')
    print(len(reporters)+len(reporter_codes)-common_count)



