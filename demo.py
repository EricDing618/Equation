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

def test():
    tool=BaseReturn()
    eq=BaseEasyEquation()

    replace_test='35 (ab++--++--+++-+3) （ab+-3）**5'
    print(tool.replace_unknown(tool.stdEq(replace_test),('a','b'),('2','3')))

    parenthesis_test='(1+5)(3+4)'
    print('Outside:',tool.sm_parenthesis(parenthesis_test)[::2])
    print('Inside:',tool.sm_parenthesis(parenthesis_test)[1::2])

    eq_main_test='  '
    eq.give(eq_main_test,debug=True)
    print('SyntaxError?:',eq.syntax_error())

if __name__=='__main__':
    test()