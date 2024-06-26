from base import *


class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def make(self):
        if len(self.tool.unknown(self.eq,self.ignore))==0: #无未知数
            return None
        else:
            left,right=self.tool.amount(self.eq) #左右分开
            if len(self.tool.unknown(left,self.ignore))==0:
                left=eval(left)
            elif len(self.tool.unknown(right,self.ignore))==0:
                right=eval(right)
            
