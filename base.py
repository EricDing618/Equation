import string,re
class Base:
    def __init__(self):
        self.operator=('+','-','*','/','=','^','.',' ') #目前支持的运算符

class BaseEasyEquation(Base):
    def __init__(self):
        super().__init__()
        self.degree=0 #元数
        self.order=0 #次幂数
        self.result=0 #结果
        self.tool=BaseReturn()
    def give(self,e,ignore=()):
        self.eq:str=e
        self.ignore:tuple=ignore
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
        cache:set={}
        num:list=[]
        last_num_index:int=0
        for i in range(len(e)):
            if e[i] in string.ascii_letters and e[i] not in ignore:
                if i==0:
                    cache.add(e[i])
                else:
                    if e[i-1] in string.digits
            elif (
                e[i] in string.digits
                and 0<=i-1
                and len(e)>=i+1
                ):
                if e[i-1] not in string.digits: #上一个字符不是数字
                    num.append(e[i])
                else:
                    if e[i+1] not in 
                    num[-1]+=e[i]

        return tuple(cache)
    def others(self,e:str):
        cache:list
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