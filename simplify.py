from base import BaseReturn
import string

class Simplify:
    def __init__(self):
        self.tool=BaseReturn()
    def sim_left(self,el):
        if len(el)==1: #没有大括号项
            el=''.join(el)
            el=self.tool.mid_parenthesis(el)
            if len(el)==1: #没有中括号项
                el=''.join(el)
                el=self.tool.sm_parenthesis(el)
                if len(el)==1: #没有小括号项
                    el=self.tool.plus(el)
                    
    def equation(self,left:str,right:str):
        el=left;er=right #左边项与右边项
        el=self.tool.big_parenthesis(el)
    
