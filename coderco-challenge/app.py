import os
from flask import Flask
import redis
import socket

app = Flask(__name__)

# Bonus: Read Redis connection details from environment variables
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))

# Connect to Redis
cache = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def welcome():
    # socket.gethostname() helps us see which container answered (useful for the scaling bonus!)
    return f"Welcome to the Multi-Container Flask App! Served by container: {socket.gethostname()}"

@app.route('/count')
def count():
    try:
        # Increment the 'hits' key in Redis
        visits = cache.incr('hits')
        return f"Visit count: {visits} (Served by: {socket.gethostname()})"
    except redis.RedisError as e:
        return f"Redis connection error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)