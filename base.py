import string,re
class Base:
    def __init__(self):
        self.operator = ('+','-','*','/','=','^','.',' ') #目前支持的运算符
        self.parenthesis = '()[]{}' #括号

class BaseEasyEquation(Base):
    def __init__(self):
        super().__init__()
        self.degree=0 #元数
        self.order=0 #次幂数
        self.result=0 #结果
        self.tool=BaseReturn()
    def give(self,e:str,ignore=(),value=()):
        self.eq = e
        if len(ignore) != len(value):
            raise ValueError("len(ignore) != len(value).")
        elif ignore and value:
            self.ignore:tuple=ignore
            self.ignore_value:tuple=value
            for v in range(len(self.ignore_value)):
                

    def type_(self):
        return self.__class__.__name__
    def syntax_error(self):
        #print(self.tool.sm_parenthesis('3[a+1]*b'))
        if (
            len(self.tool.amount(self.eq)) != 2 #等号错误
            or self.tool.highest_power(self.eq) != self.order #次幂不符
            or len(self.tool.unknown(self.eq,self.ignore)) != self.degree #未知数数量不符
            or len(self.tool.others(self.eq)) > 0 #含有与方程无关的字符
            or self.tool.parenthesis_error(self.eq) #括号个数不对称
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
    def big_parenthesis(self,e:str):
        c1=e.split('{')
        c2:list=[]
        for i in range(len(c1)):
            c3=c1[i].split("}")
            for j in range(len(c3)):
                c2.append(c3[j])
        return c2
    def mid_parenthesis(self,e:str):
        c1=e.split('[')
        c2:list=[]
        for i in range(len(c1)):
            c3=c1[i].split("]")
            for j in range(len(c3)):
                c2.append(c3[j])
        return c2
    def sm_parenthesis(self,e:str):
        c1=e.split('(')
        c2:list=[]
        for i in range(len(c1)):
            c3=c1[i].split(")")
            for j in range(len(c3)):
                c2.append(c3[j])
        return c2
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
    def collect(self,e:str):
        _return=[]
        c1=''.join(e.split(' ')) #过滤空格
        for i1 in self.plus(c1):
            for i2 in self.less(i1):
                for i3 in self.times(i2):
                    for i4 in self.divide(i3):
                        for i5 in range(len(i4)-1):
                            if (i4[i5] in string.digits+string.ascii_letters+self.parenthesis) and (i4[i5+1] in string.ascii_letters+string.ascii_letters+self.parenthesis) and not(i4[i5] in string.digits and i4[i5+1] in string.digits):

    def others(self,e:str):
        cache:list=[]
        for i in range(len(e)):
            if e[i] not in string.ascii_letters+string.digits+''.join(self.operator):
                cache.append(e[i])
        return tuple(cache)
    def parenthesis_error(self,e:str):
        if (
            len(re.findall('\(+',e))==len(re.findall('\)+',e))
            and len(re.findall('\[+',e))==len(re.findall('\]+',e))
            and len(re.findall('\{+',e))==len(re.findall('\}+',e))
        ):
            return False
        else:
            return True