def start_end_decorator(func):
  def wrapper():
    print('Start')
    func()
    print('End')
  return wrapper

def print_name():
  print('Joel')

print_name()
print_name= start_end_decorator(print_name)
print_name()

@start_end_decorator
def print_name():
    print('Joel')
    
print_name()

def start_end_decorator(func):
    
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result               
    return wrapper

@start_end_decorator
def add_5(x):
    return x + 5

result = add_5(10)
print(result)


import functools
def start_end_decorator(func):
    
    @functools.wraps(func)                            
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add_5(x):                                         
    return x + 5
result = add_5(35)
print(result)
print(add_5.__name__)


#class decorator

import functools

class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(num):
    print("Hello!")
    
say_hello(5)
say_hello(5)
