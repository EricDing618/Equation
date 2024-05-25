import string

class Base:
    def __init__(self):
        self.operator=('+','-','*','/','=','^','.',' ') #目前支持的运算符

class BaseEasyEquation(Base):
    def __init__(self):
        super().__init__()
        self.degree=0 #元数
        self.order=0 #次幂数
        self.tool=BaseReturn()
    def give(self,e,ignore=()):
        self.eq:str=e
        self.ignore:tuple=ignore
    def type_(self):
        return self.__class__.__name__
    def syntax_error(self):
        if (
            len(self.tool.amount(self.eq)) != 2
            or self.tool.highest_power(self.eq) != self.order
            or len(self.tool.unknown(self.eq,self.ignore)) != self.degree
            or len(self.tool.others(self.eq)) > 0
            ):
            return True
        else:
            return False
        
class BaseReturn(Base):
    def __init__(self):
        super().__init__()
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
    def unknown(self,e:str,ignore:tuple):
        cache=set()
        for i in range(len(e)):
            if e[i] in string.ascii_letters and e[i] not in ignore:
                cache.add(e[i])
        return tuple(cache)
    def others(self,e:str):
        cache=[]
        for i in range(len(e)):
            if e[i] not in string.ascii_letters+string.digits+''.join(self.operator):
                cache.append(e[i])
        return tuple(cache)

class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def get(self,e:str):
        pass

def demo():
    print(OneOne().type_())

    a=OneOne()

    a.give('ax+1')
    print(a.syntax_error())

    a.give('ax+1=b')
    print(a.syntax_error())

    a.give('ax+1=b',ignore=('a','b'))
    print(a.syntax_error())

    a.give('x+2=1')
    print(a.syntax_error())

if __name__=="__main__":
    demo()