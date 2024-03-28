def some_checker(func):
    def wrapper(*args, **kwargs):
        for val in args:
                 if type(val) != int:
                      raise TypeError('Argument a must be int, not str')
        for key, val in kwargs.items():
                 if type(val) != int:
                      raise TypeError('Argument a must be int, not str')
        result = func(*args, **kwargs)
        if not isinstance(result, int):
              raise TypeError('Failure of cheking the return type')
        return result
    return wrapper                                                      
           
@some_checker
def add(a: int, b: int) -> int:
    return a + b   

add(1, 2)
