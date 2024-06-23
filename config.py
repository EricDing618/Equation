import string

OPERATOR = '+-*/=^. ' #目前支持的符号
PARENTHESIS = '()[]{}' #括号
LETTERS = string.ascii_letters
NUMBERS = string.digits
ALL = OPERATOR+PARENTHESIS+LETTERS+NUMBERS #所有合法的字符