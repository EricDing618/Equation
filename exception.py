class EquationSyntaxError(SyntaxError):
    def __init__(self,args:str=None):
        self.info=args
    def __str__(self):
        if self.info:
            return self.info
        else:
            return "Invalid input data."