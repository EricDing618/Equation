from base import BaseReturn
import string

class Simplify:
    def __init__(self):
        self.tool=BaseReturn()
    def easy_eq(self,left:str,right:str): #指像x+2=3这样的方程
        if 
    def equation(self,left:str,right:str):
        cl=left;cr=right #左边项与右边项
        cl=self.tool.big_parenthesis(cl)
        if len(cl)==1: #没有大括号项
            cl=''.join(cl)
            cl=self.tool.mid_parenthesis(cl)
            if len(cl)==1: #没有中括号项
                cl=''.join(cl)
                cl=self.tool.sm_parenthesis(cl)
                if len(cl)==1: #没有小括号项
