from equation import *

def demo():
    a=OneOne()

    while True:
        enter=input('> ')
        cmd=enter.split(' ',1)
        match cmd[0]:
            case "type":
                print(a.type_())
            case "give":
                a.give(cmd[1])
            case "giveig":
                c=cmd[1].rsplit(" ",1)
                a.give(c[0],tuple(c[1].split(",")))
            case "check":
                print("Wrong: "+str(a.syntax_error()))
            case "get":
                if a.syntax_error():
                    print('Invalid input data.')
                else:
                    print(a.get())

class tests():
    def __init__(self):
        self.tool=BaseReturn()
        self.eq=BaseEasyEquation()

    def replace_test(self,e='35 (ab++--++--+++-+3) （ab+-3）**5',ignore=('a','b'),value=('2','3')):
        return self.tool.replace_unknown(self.tool.stdEq(e),ignore,value)

    def parenthesis_test(self,e='(1+5)(3+4)'):
        return f'Outside: {self.tool.sm_parenthesis(e)[::2]}\nInside: {self.tool.sm_parenthesis(e)[1::2]}'

    def syntax_test(self,e='  '):
        self.eq.give(e,debug=True)
        return f'SyntaxError?: {self.eq.syntax_error()}'

    def level_test(self,e='a+1=2',ignore=()):
        return self.tool.level(e,ignore)

if __name__=='__main__':
    eqs=['1+1=2','a=1','a+1=2','a*2+1=3','a*(2+1)=3','a*(2/1^2)=2','(a^2)*(2+1)=3','{a+1*[(3-2)^2]}=2']
    print_info={}
    test=tests()
    for eq in eqs:
        print_info[eq]=test.level_test(test.replace_test(eq,(),()),())
    print(print_info)