def user_role(role):
    def decorator(func):
        def wrapper(**kwargs):
            user_type = kwargs.get('user_type')  
            if user_type != role:  
                raise ValueError("Permission denied")  
            return func(**kwargs)  
        return wrapper  
    return decorator  


@user_role('admin')
def show_customer_receipt(**kwargs):
    print("Welcome boss")

try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e)  

show_customer_receipt(user_type='admin')     

