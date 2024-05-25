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
    def check_syntax(self):
        if len(self.tool.amount(self.eq)) != 2:
            raise SyntaxError
        elif self.tool.highest_power(self.eq) != self.order:
            raise SyntaxError
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
    def 

class OneOne(BaseEasyEquation):
    def get(self,e:str):
        pass

print(OneOne().type_())