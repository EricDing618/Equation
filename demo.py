from equation import *
import pprint

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
        '''return (outside,inside)'''
        return self.tool.sm_parenthesis(e)[::2],self.tool.sm_parenthesis(e)[1::2]

    def syntax_test(self,e='  ',debug=True):
        '''return (syntax error?:) bool'''
        self.eq.give(e,debug=debug)
        return self.eq.syntax_error()

    def level_test(self,e='a+1=2',ignore=(),more=False):
        if more:
            return self.tool.level(e,ignore)
        else:
            return self.tool.level(e,ignore)[0]

if __name__=='__main__':
    print_info={}
    test=tests()

    def check_syntax(e,ignore=(),value=()):
        if not test.syntax_test(test.replace_test(e,ignore,value),True):
            return 'ok'
        else:
            return 'error'

    def many_eqs(eqs:Union[list[str],tuple[str]]=['1+1=2','a=1','a+1=2','a*2+1=3','a*(2+1)=3','a*(2/1^2)=2','(a^2)*(2+1)=3','{a+1*[(3-2)^2]}=2']):
        for eq in eqs:
            print_info[eq] ={
                'Level':test.level_test(test.replace_test(eq,(),()),()),
                'Syntax':check_syntax(eq,(),())
                }
        pprint.pprint(print_info,width=4,indent=2,sort_dicts=False)

    def one_eq(eq=''):
        print_info[eq] ={
            'Level':test.level_test(test.replace_test(eq,(),()),()),
            'Syntax':check_syntax(eq,(),())
            }
        pprint.pprint(print_info,width=4,indent=2,sort_dicts=False)

    one_eq('23=a-2+1')