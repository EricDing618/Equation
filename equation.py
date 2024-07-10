from base import *

class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def make(self): #最后赋值给self.result，不是return
        eq_level=self.tool.level(self.eq)
        match eq_level:
            case 1:
                pass
        
            
