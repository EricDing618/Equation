import re
from typing import Union
from config import *
from exception import *

class Base:
    def __init__(self):
        self.tool=BaseReturn()

class BaseEasyEquation(Base):
    def __init__(self):
        super().__init__()
        self.degree=0 #元数
        self.order=0 #次幂数
        self.result:Union[int,dict,None] #结果（一元：int，多元：dict）
        self.eq='' #方程
        self.ignore=() #忽略的未知数
        self.value=() #忽略数的值

    def make(self):
        print(f'equation: {self.eq}')
        print(f'result: {self.result}')

    def give(self,e:str,ignore:tuple=(),value:tuple=()):
        self.eq = e
        self.ignore=ignore
        self.value=value
        if len(self.ignore) != len(self.value): #忽略数与忽略数的值个数不相等
            raise EquationSyntaxError
        else:
            self.eq.replace('**','^') #防止误判为乘号，使用eval()时应将“^”转回为“**”！
            self.eq=self.tool.stdEq(self.eq)
            self.eq=self.tool.replace_unknown(self.eq,self.ignore,self.value)
            if self.syntax_error(): #语法错误
                raise EquationSyntaxError
            elif len(self.tool.unknown(self.eq,self.ignore))==0: #无未知数
                self.result=None
            else:
                self.make() #给出结果

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
            or self.tool.SymbolIsConnect(self.eq) #符号相连
            ):
            return True
        else:
            return False
        
    def get(self):
        return self.result #返回结果
    

class BaseReturn():
    '''e: str= Equation String'''
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
    
    def include_parenthesis(self,e:str,type_:int):
        '''type_: int
        = 0: Big parenthesis
        = 1: Middle parenthesis
        = 2: Small parenthesis'''
        match type_:
            case 0:
                return '{' in e and '}' in e
            case 1:
                return '[' in e and ']' in e
            case 2:
                return '(' in e and ')' in e
            case _:
                raise SyntaxError
            
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
            if e[i] in LETTERS and e[i] not in ignore:
                cache.add(e[i])
        return tuple(cache)
    
    def SymbolIsConnect(self,e:str):
        return_=False
        for i in range(len(e)-1):
            if (e[i] in OPERATOR and e[i+1] in OPERATOR) or (e[i] in LEFTPARENTHESIS and e[i+1] in RIGHTPARENTHESIS):
                return_=True
                break
        return return_
    def plus_less(self, e: str):
        '''将加法和减法混合的符号化简'''
        c1 = e
        while ('+-' in c1) or ('-+' in c1) or ('++' in c1) or ('--' in c1):
            c1 = c1.replace('+-', '-').replace('-+', '-').replace('++', '+').replace('--', '+')
        return c1
        
    def stdEq(self,e:str):
        '''方程标准化'''
        c1=e
        c2=[]
        # 去除多余空格，更正全角为半角符号
        c1=c1.replace(' ','').replace('（','(').replace('）',')')
        # 去除多余符号
        c1=self.plus_less(c1)
        # 括号间添加乘号
        for r in RIGHTPARENTHESIS:
            for l in LEFTPARENTHESIS:
                c1=c1.replace(r+l,r+'*'+l)
        c1=c1.replace('**','^') #防止误判为乘号，使用eval()时应将“^”转回为“**”！
        #第二次添加乘号
        for i in range(len(c1)-1):
            front=c1[i];back=c1[i+1]
            if (
                (front in LETTERS and back in LETTERS)
                or (front in LETTERS and back in NUMBERS)
                or (front in NUMBERS and back in LETTERS)
                or (front in NUMBERS and back in LEFTPARENTHESIS)
                or (front in RIGHTPARENTHESIS and back in NUMBERS)
                ):
                c2.append(front+'*'+back)
            else:
                c2.append(front+back)
        for i in range(len(c2)):
            if i != 0:
                c2[i]=c2[i][1:]
        return ''.join(c2)

    def replace_unknown(self,e:str,ignore:tuple,value:tuple):
        cache=e
        for ign,val in zip(ignore,value):
            cache=cache.replace(ign,str(val))
        return cache
    
    def others(self,e:str):
        cache:list=[]
        for i in range(len(e)):
            if e[i] not in ALL:
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
        

    #被废弃的方法 
    def _old__plus_less(self,e:str):
        '''将加法和减法混合的符号化简'''
        c1=e
        c2=True
        c3=0
        while c2:
            c1 = c1.replace('+-', '-').replace('-+', '-').replace('++', '+').replace('--', '+')
            for i in ('++','--','+-','-+'):
                if i not in c1:
                    c3+=1
                else:
                    c3-=1
            if c3>=4: #保险起见，设置范围
                c2=False
                return c1