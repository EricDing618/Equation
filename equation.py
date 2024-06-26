from base import *

class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def make(self): #最后赋值给self.result
        left,right=self.tool.amount(self.eq) #左右分开
        if len(self.tool.unknown(left,self.ignore))==0:
            left=str(eval(left))
        elif len(self.tool.unknown(right,self.ignore))==0:
            right=str(eval(right))
        else:
            left=self.tool.simplification_parenthesis(left,self.ignore)
            right=self.tool.simplification_parenthesis(right,self.ignore)
            
