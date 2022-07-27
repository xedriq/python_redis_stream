import redis
from datetime import datetime
import time

r = redis.Redis(host='0.0.0.0', port=6379, db=1, decode_responses=True)

data = r.xread({'checkins': '$'}, 10, 0)
print(data)