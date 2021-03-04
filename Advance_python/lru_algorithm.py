#  Date: 3/4/21, 08:54 AM
#  Author: dharapx
#  Feel free to use this code
import time
from functools import lru_cache

'''
maxsize attribute that defines the maximum number of entries before the cache starts evicting old items. 
By default, maxsize is set to 128. If you set maxsize to None, then the cache will grow indefinitely, 
and no entries will be ever evicted.
'''
@lru_cache(maxsize=16)
def fibonacci_series(n):
    """
    Computing Fibonacci Series: 
    The first two terms are 0 and 1. 
    All other terms are obtained by adding the preceding two terms. 
    This means to say the nth term is the sum of (n-1)th and (n-2)th term.
    :param n: any number
    :return: integer
    """
    if n <= 1:
        return n
    else:
        x = fibonacci_series(n - 1) + fibonacci_series(n - 2)
        # print(x)
        return x


s_time = time.time()
for x in range(20):
    print(f"Calculating for number: {x} \n {fibonacci_series(x)}")
e_time = time.time()
print(f"Execution time: {e_time - s_time} seconds")
