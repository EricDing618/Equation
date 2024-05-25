import string

class BaseEasyEquation:
    def __init__(self):
        self.degree=0 #元数
        self.order=0 #次幂数
        self.operator=('+','-','*','/','=','>','<','^') #目前支持的运算符
        self.tool=BaseReturn()
    def give(self,e):
        self.eq:str=e
    def type_(self):
        return self.__class__.__name__
    def syntax_error(self):
        if (
            len(self.tool.amount(self.eq)) != 2
            or self.tool.highest_power(self.eq) != self.order
            or len(self.tool.unknown(self.eq)) != self.degree
            ):
            return True
        else:
            return False
        
class BaseReturn():
    def plus(self,e:str):
        return e.split('+')
    def less(self,e:str):
        return e.split('-')
    def times(self,e:str):
        return e.split('*')
    def divide(self,e:str):
        return e.split('/')
    def amount(self,e:str):
        return e.split('=')
    def highest_power(self,e:str)->int:
        cache=e.split('^')
        if len(cache) > 1:
            for i in range(1,len(cache)):
                cache[i]=int(cache[i][0])
            del cache[0]
            cache=max(cache)
            return cache
        else:
            return 1
    def unknown(self,e:str):
        cache=set()
        for i in range(len(e)):
            if e[i] in string.ascii_letters:
                cache.add(e[i])
        return tuple(cache)

class OneOne(BaseEasyEquation):
    def get(self,e:str):
        pass

print(OneOne().type_())