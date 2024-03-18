import time
from ratelimit import limits, RateLimitException

@limits(calls=2, period=60)
def some_funct():
    print('Please dont rush!')
    pass



try:
    some_funct()
    
except RateLimitException as e:
    print("Превышен лимит скорости:", e)

