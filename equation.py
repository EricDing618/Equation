from base import *

class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def make(self): #最后赋值给self.result，不是return
        left,right=self.tool.amount(self.eq) #左右分开
        if len(self.tool.unknown(left,self.ignore))==0: #左边没有未知数
            left=str(eval(left))
        elif len(self.tool.unknown(right,self.ignore))==0: #右边没有未知数
            right=str(eval(right))
        else: #两边都有未知数

            #处理左边
            if self.tool.include_parenthesis(left,0): #含有大括号
                left=self.tool.big_parenthesis(left)
                for i in left[::2]: #括号外
                    if i:
                        if i[-1] in ('*','/'): #和括号内有乘除关系
                            pass
                        elif i[-1] in ('+','-'): #和括号内有加减关系
                            pass
                        else: #其他关系，如括号内次幂，未来考虑
                            raise EquationFutureWarning

            
