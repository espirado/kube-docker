import time
import redis
import socket
from flask import Flask, request ,jsonify,make_response

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/', methods=['GET'])
def return_hostname():
     sucess = 200
     count = get_hit_count()
     return jsonify(" hits: {}".format(count),"sucess:True", " hostname   : {} ".format(socket.gethostname()))

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
