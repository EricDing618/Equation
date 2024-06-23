import string

OPERATOR = '+-*/=^. ' #目前支持的符号
LEFTPARENTHESIS = '([{' #左括号
RIGHTPARENTHESIS = ')]}' #右括号
PARENTHESIS = LEFTPARENTHESIS+RIGHTPARENTHESIS #括号
LETTERS = string.ascii_letters
NUMBERS = string.digits
ALL = OPERATOR+PARENTHESIS+LETTERS+NUMBERS #所有合法的字符