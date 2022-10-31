import time
from typing import Callable

def timeme(func):
    def wrapper():
        start = time.time()
        func()
        print(f"Total time {time.time() - start}")
    return wrapper
