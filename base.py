import re
import math
import sympy as sp
#import decimal
from typing import Union
from config import *
from exception import *

class Base:
    def __init__(self):
        ''':param e: 方程式字符串'''


class OldTools(Base):
    '''被废弃的方法,方法名：_old__+原名称''' 
    def _old__simplification_add_subtract(self,e:str):
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
            
    def _old__highest_power(self, e: str, ignore=()) -> int:
        cache = e.split('^')
        if len(cache) > 1:
            cache = [int(x) if x else None for x in cache[1:]]
            cache = [x for x in cache if x is not None]  # 过滤掉空字符串
            return max(cache, key=cache.index) if cache else 0
        elif len(self.unknown(e, ignore)):
            return 1
        else:
            return 0
        

class stdTools(Base):
    def simplification_add_subtract(self, e: str):
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
        c1=self.simplification_add_subtract(c1)
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
    

class EasyTools(Base):
    def __init__(self):
        '''
        :param e: 方程式字符串
        :param mode: 返回模式，0:返回分割内容 1:返回符号个数
        '''

    def add(self,e:str,mode=0):
        c1=e.split('+')
        match mode:
            case 0:
                return c1
            case 1:
                return len(c1)-1
            case _:
                raise SyntaxError
    def subtract(self,e:str,mode=0):
        c1=e.split('-')
        match mode:
            case 0:
                return c1
            case 1:
                return len(c1)-1
            case _:
                raise SyntaxError
    def multiply(self,e:str,mode=0):
        c1=e.split('*')
        match mode:
            case 0:
                return c1
            case 1:
                return len(c1)-1
            case _:
                raise SyntaxError
    def divide(self,e:str,mode=0):
        c1=e.split('/')
        match mode:
            case 0:
                return c1
            case 1:
                return len(c1)-1
            case _:
                raise SyntaxError
    
    def equals(self,e:str,mode=0):
        c1=e.split('=')
        match mode:
            case 0:
                return c1
            case 1:
                return len(c1)-1
            case _:
                raise SyntaxError


class ParenthesisTools(Base):
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
    
    def include_parenthesis(self,e:str,type_:Union[int,tuple,list]):
        '''type_: int| tuple| list
        = 0: Big parenthesis
        = 1: Middle parenthesis
        = 2: Small parenthesis
        = 3: Any parenthesis
        = 4: All parenthesis'''
        def return_(type_):
            match type_:
                case 0:
                    return '{' in e and '}' in e
                case 1:
                    return '[' in e and ']' in e
                case 2:
                    return '(' in e and ')' in e
                case 3:
                    return ('{' in e and '}' in e) or ('[' in e and ']' in e) or ('(' in e and ')' in e)
                case 4:
                    return ('{' in e and '}' in e) and ('[' in e and ']' in e) and ('(' in e and ')' in e)
                case _:
                    raise SyntaxError
                
        if isinstance(type_,int):
            return return_(type_)
        elif isinstance(type_,(tuple,list)):
            c1=[]
            for i in type_:
                if i not in (0,1,2):
                    raise SyntaxError
                else:
                    c1.append(return_(type_))
            return (False not in c1)
        else:
            raise SyntaxError



class BaseEquation(Base):
    def __init__(self):
        self.tool=BaseReturn()

class BaseEasyEquation(BaseEquation):
    def __init__(self):
        super().__init__()
        self.degree=0 #元数
        self.order=0 #次幂数
        self.result:Union[dict[str,Union[int,tuple]],None]=None #结果（一元：int，多元：dict）
        self.eq='' #方程
        self.ignore=() #忽略的未知数
        self.value=() #忽略数的值

    def make(self):
        '''解方程核心方法'''
        #print(f'equation: {self.eq}')
        #print(f'result: {self.result}')

    def give(self,e:str,ignore:tuple=(),value:tuple=(),debug=False):
        """
        :param ignore: 要忽略的字母，可以是常数或系数。
        :param value: 忽略的字母对应的值。
        :param debug: False时，方程有语法错误将报错，否则停止运行并可以使用其他函数（详见`demo.py`）
        :return: None
        """
        self.eq = e
        self.ignore=ignore
        self.value=value
        self.debug=debug
        if len(self.ignore) != len(self.value): #忽略数与忽略数的值个数不相等
            raise EquationSyntaxError
        else: #注意调用函数的顺序（转换幂运算符 ->标准化方程 ->替换未知数），否则会出现BUG！
            self.eq.replace('**','^') #防止误判为乘号，使用eval()时应将“^”转回为“**”！
            self.eq=self.tool.stdEq(self.eq)
            self.eq=self.tool.replace_unknown(self.eq,self.ignore,self.value)
            if self.syntax_error(): #语法错误
                if not self.debug:
                    raise EquationSyntaxError
            elif len(self.tool.unknown(self.eq,self.ignore))==0: #无未知数
                self.result=None
            else:
                self.left,self.right=self.tool.equals(self.eq) #左右分开
                self.make() #给出结果

    def type_(self):
        return self.__class__.__name__
    
    def syntax_error(self):
        if (
            self.tool.equals(self.eq,1) != 1 #等号错误
            or (self.tool.highest_power(self.eq) != self.order and not self.debug) #次幂不符
            or (len(self.tool.unknown(self.eq,self.ignore)) != self.degree and not self.debug) #未知数数量不符
            or len(self.tool.others(self.eq)) > 0 #含有与方程无关的字符
            or self.tool.parenthesis_error(self.eq) #括号个数不对称
            or self.tool.SymbolIsConnect(self.eq) #符号相连
            ):
            return True
        else:
            return False
        
    def get(self):
        return self.result #返回结果
    

class BaseReturn(EasyTools,ParenthesisTools,stdTools,OldTools):
    def __init__(self):
        super().__init__()

    def eq_eval(self,e:str):
        if len(self.others(e)) > 0:
            return None
        else:
            return eval(e)

    def highest_power(self,e:str,ignore=())->int:
        cache=e.split('^')
        intc=[]
        if len(cache) > 1:
            for i in range(1,len(cache)):
                #cache[i]=int(cache[i][0])
                if cache[i] is not None:
                    intc.append(int(cache[i][0]))
            #del cache[0]
            #cache=max(cache)
            #return cache
            return max(intc)
        elif len(self.unknown(e,ignore)) > 0:
            return 1
        else:
            return 0
               
    def unknown(self,e:str,ignore:tuple):
        '''返回所有未知数'''
        cache=set()
        for i in range(len(e)):
            if e[i] in LETTERS and e[i] not in ignore:
                cache.add(e[i])
        return tuple(cache)
    
    def SymbolIsConnect(self,e:str):
        '''运算符是否有相连的情况'''
        return_=False
        for i in range(len(e)-1):
            if (e[i] in OPERATOR and e[i+1] in OPERATOR) or (e[i] in LEFTPARENTHESIS and e[i+1] in RIGHTPARENTHESIS):
                return_=True
                break
        return return_
    
    def others(self,e:str):
        '''和方程无关的字符'''
        cache:list=[]
        for i in range(len(e)):
            if e[i] not in ALL:
                cache.append(e[i])
        return tuple(cache)
    
    def parenthesis_error(self,e:str):
        '''括号是否不对称'''
        if (
            len(re.findall(r'\(+',e))==len(re.findall(r'\)+',e))
            and len(re.findall(r'\[+',e))==len(re.findall(r'\]+',e))
            and len(re.findall(r'\{+',e))==len(re.findall(r'\}+',e))
        ):
            return False
        else:
            return True
    
    def level(self,e:str,ignore:tuple):
        '''方程难度等级'''
        l = 0
        more_info={ #详细信息
            "unknown":self.unknown(e,ignore),
            "parenthesis":{
                "all":self.include_parenthesis(e,4),
                "any":self.include_parenthesis(e,3)
            },
            "highest_power":self.highest_power(e),

            "add_or_subtract":self.add(e,1) > 0 or self.subtract(e,1) > 0,
            "add":self.add(e,1),
            "subtract":self.subtract(e,1),

            "multiply_or_divide":self.multiply(e,1) > 0 or self.divide(e,1) > 0,
            "multiply":self.multiply(e,1),
            "divide":self.divide(e,1)
        }

        if len(more_info['unknown']) > 0:
            l+=1
            if more_info['parenthesis']['all']:
                l+=2
            elif more_info['parenthesis']['any']:
                l+=1
            
            if more_info['highest_power'] > 1:
                l+=2

            if more_info['add_or_subtract']:
                l+=1
            if more_info['multiply_or_divide']:
                l+=1

        return l,more_info