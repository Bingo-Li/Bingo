# import sys
# import requests
# class ff(object):
#     @staticmethod
#     def runx():
#         print(requests.get('http://www.baidu.com').status_code)

# #ff.runx()


# class gg(object):
#     def __init__(self,url,stat):
#         self.url = url
#         self.stat = stat
#     def outer(self):
#         print (self.url)
#         print (self.stat)
# a = gg('baidu',200)
# a.outer()

# class ggg(object):
#     url = 0
#     stat = 0

#     def __init__(self,url=0,stat=0):
#         self.url = url
#         self.stat = stat
#     @classmethod
#     def split(cls,info):
#         url,stat = map(str,info.split('-'))
#         data = cls(url,stat)
#         return data
#     def outer(self):
#         print (self.url)
#         print (self.stat)

# r = ggg.split(('baidu-2000'))
# r.outer()

class cc(object):
    ccc = 'cccc'
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


class animal(object):
    """描述类信息，可以被自动收集"""
    def run(self):
        print("animal is running...")
    """bingo"""
def run_twice(ani):
    ani.run()
    ani.run()
    
        
class dog(animal):
    pass
class cat(animal):
    pass

Dog = dog()
Dog.run()
run_twice(animal())
run_twice(dog())
print(animal.__doc__)