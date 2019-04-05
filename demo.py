#函数作为参数
import math
def add(x,y,f):
    return f(x)+f(y)
a = add(-3,4,abs)
print(a)

b = add(25,9,math.sqrt)
print(b)

def f(x):
    return x*x
c = map(f,[2,3,4,5])
print(c)

def switch(str):
    return str[0].upper+str[1:].lower
d = map(switch,['adam', 'LISA', 'BarT'])
print(d)