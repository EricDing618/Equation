class BaseEquation:
    def type_(self):
        return self.__class__.__name__

class BaseReturn():
    def plus(e:str):
        return e.split('+')
    def less(e:str):
        return e.split('-')
    def times(e:str):
        return e.split('*')
    def divide(e:str):
        return e.split('/')
    def check_syntax(e:str,class_:object):
        match class_().type_():
            case 'OneOne':
                pass

class OneOne(BaseEquation):
    def get(self,e:str):
        pass

print(OneOne().type_())