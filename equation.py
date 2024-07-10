from base import *

class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def make(self): #最后赋值给self.result，不是return
        level=self.tool.level(self.eq)
        difficulty, more_info = level[0],level[1]
        match difficulty:
            case 0:
                self.result=None
            case 1:
                pass
        
            
