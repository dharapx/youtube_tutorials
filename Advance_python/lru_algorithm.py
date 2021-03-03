#  Date: 3/3/21, 12:54 PM
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
def fibinacci_series(n):
    '''
    computing fibinacci_series for given number
    '''
    if n <= 1:
        return n
    else:
        return fibinacci_series(n - 1) + fibinacci_series(n - 2)


s_time = time.time()
print([fibinacci_series(x) for x in range(40)])
e_time = time.time()
print(e_time - s_time)
