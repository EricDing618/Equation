from equation import *
#print(OneOne().type_())
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
            print("State: "+str(a.syntax_error()))
        case "get":
            if a.syntax_error():
                print('Invalid input data.')
            else:
                print(a.get())