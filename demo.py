from equation import *
#print(OneOne().type_())

a=OneOne()

a.give('ax+1')
print(a.syntax_error())

a.give('ax+1=b')
print(a.syntax_error())
a.get()

a.give('ax+1=b',ignore=('a','b'))
print(a.syntax_error())

a.give('x+2=1')
print(a.syntax_error())
a.get()