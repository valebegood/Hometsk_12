#1. Напишите декоратор, который обеспечивает вызов функции только пользователями с определенной ролью. 
#Каждая функция должна иметь тип user_type со строковым типом в kwargs. Пример:

def is_role(role):
    def decorator(func):
        def wrapper(**kwargs):
            user_type = kwargs.get('user_type')  
            if user_type != role:  
                raise ValueError("Permission denied")  
            return func(**kwargs)  
        return wrapper  
    return decorator  

@is_role('admin')
def show_customer_receipt(**kwargs):
    print("Receipt shown")

