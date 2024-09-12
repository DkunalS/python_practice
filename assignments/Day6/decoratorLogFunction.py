import logging
import time
from functools import wraps

logging.basicConfig(filename='decoratorExampleLog.log', 
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Function {func.__name__} called')
        return func(*args, **kwargs)
    return wrapper

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f'Function {func.__name__} executed in {execution_time:.4f} seconds')
        return result
    return wrapper

@log_function
@log_execution_time
def example_function(n):
    count_value = 0
    for i in range(n):
        count_value += i
    return count_value

example_function(100000)
