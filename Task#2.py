def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Found 1 error during execution of your function: {type(error).__name__} {str(error)}")
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})