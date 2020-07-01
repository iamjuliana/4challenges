# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# SOME PYTHON
# ======================

## Python Standard Library
# https://docs.python.org/3/library/


## args and kwargs

def eggs(*args):
    for a in args:
        print(a)

# eggs(12, 'omelette', 9.6)

def pan(**kwargs):
    print(kwargs)

# pan(a=1, b=2, c='three')

