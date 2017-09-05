
#encoding=utf-8


import sys

def div(x, y):
    try:
        return x/y
    except:
        tb = sys.exc_info()  # return (exc_type, exc_value, traceback)
        print tb
        #print tb.tb_lineno      # "return x/y" 的行号
div(1, 0)
