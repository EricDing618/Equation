from base import *


class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def make(self):
        if len(self.tool.unknown(self.eq,self.ignore))==0:
            return None
        else:
            left,right=self.tool.amount(self.eq)
            
