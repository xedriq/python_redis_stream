import redis
from datetime import datetime
import time
import random

r = redis.Redis(host='0.0.0.0', port=6379, db=1)
user_id = random.randint(1, 1000)
venue_id = random.randint(100, 400)
star_rating = random.randint(1, 5)
my_data = {'user_id':user_id, 'venue_id':venue_id, 'star_rating':star_rating}

while True:
    user_id = random.randint(1, 1000)
    venue_id = random.randint(100, 400)
    star_rating = random.randint(1, 5)
    my_data = {'user_id':user_id, 'venue_id':venue_id, 'star_rating':star_rating}
    
    r.xadd('checkins', {'data': str(my_data), 'date_today': datetime.today().strftime("%d/%m/%Y %H:%M:%S")})
    secs = random.randint(1,5)
    time.sleep(secs)