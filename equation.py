from base import *


class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数

    def get(self):
        if self.syntax_error(): #首先检查语法是否有误
            raise SyntaxError("Invalid input data.")
        else:
            self.result=self.tool.amount(self.eq)
