def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def expensive_function(x):
    print
    return x * x
print(expensive_function(5))  
print(expensive_function(5),'cache result') 