from base import *

class OneOne(BaseEasyEquation):
    def __init__(self):
        super().__init__()
        self.degree=1 #元数
        self.order=1 #次幂数
    def __level2(self):
        pass
    def __level3(self):
        pass
    def __level4(self):
        pass
    def __level5(self):
        pass
    def __level6(self):
        pass
    def __level7(self):
        pass
    def make(self): #最后赋值给self.result，不是return
        level=self.tool.level(self.eq,self.ignore)
        difficulty, more_info = level[0],level[1]
        match difficulty:
            case 0:
                self.result=None
            case 1:
                if self.left in LETTERS:
                    if self.right in LETTERS:
                        raise EquationSyntaxError
                    else:
                        self.result={self.left:sp.sympify(self.right)}
                elif self.right in LETTERS:
                    self.result={self.right:sp.sympify(self.left)}
                else:
                    raise EquationSyntaxError
            case 2:
                self.__level2()
            case 3:
                self.__level3()
            case 4:
                self.__level4()
            case 5:
                self.__level5()
            case 6:
                self.__level6()
            case 7:
                self.__level7()
            case _:
                raise EquationFutureWarning
        
if __name__=='__main__':
    eq=OneOne()
    eq.give('a=2')
    print(eq.get())
