import numpy as np, json, argparse, subprocess, time
import redis

def cache(args):
    r = redis.Redis(host=args.host, port=args.port)

    with open(args.file, 'r') as f:
        data = json.loads(f.read())
    assert len(data) > 300

    idx_l = np.random.choice(len(data), 300)

    # DON'T MODIFY THIS PART
    if args.stage == 'prod':
        global pid
        arguments = vars(args)
        arguments.update({"idx_l": idx_l.tolist()})
        with open('arguments.json', 'w') as f:
            f.write(json.dumps(arguments))
        pid = subprocess.Popen(["python3", "exec.py", "--name", __file__])

    for i in idx_l:
        # YOUR CODE GOES HERE
        if not r.exists(data[i]['code']):
            capacity = 10 - r.llen('cache')
            if capacity <= 0:
                id = r.rpop('cache')
                r.delete(id)
            r.lpush('cache', data[i]['code'])
            r.set(data[i]['code'], data[i]['summary'])
        # YOUR CODE ENDS HERE
        time.sleep(0.5)


if __name__ == "__main__" :

    ap = argparse.ArgumentParser()
    ap.add_argument('--host', default='localhost', help='Redis server host', required=False, type=str)
    ap.add_argument('--port', default='6379', help='Redis server port', required=False, type=str)
    ap.add_argument('--file', help='Path to data file', required=True, type=str)
    ap.add_argument('--type', choices=['json', 'csv'], default='json', help='Type of file data are stored in.', required=False)
    ap.add_argument('--stage', choices=['prod', 'dev'], default='dev', required=False)

    args = ap.parse_args()

    cache(args)

    if args.stage == 'prod':
        pid.wait()
