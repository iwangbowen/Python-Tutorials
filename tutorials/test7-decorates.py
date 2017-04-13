def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

# equals to display = decorator_function(display)
@decorator_function 
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

# decorated_display = decorator_function(display)

# decorated_display()

display()

display_info('Bowen', 25)

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename = '{}.log'.format(orig_func.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    
    return wrapper

@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Bowen', 25)