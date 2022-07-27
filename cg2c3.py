import redis
from datetime import datetime
import time

r = redis.Redis(host='0.0.0.0', port=6379, db=1, decode_responses=True)

# print(r.xgroup_create(name='checkins', groupname="cg2", id='$'))
while True:
    print(r.xreadgroup(groupname='cg2',consumername='consumer3', streams={'checkins':'>'}, block=10000), "\n")
    