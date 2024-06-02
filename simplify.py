from base import BaseReturn
import string

class Simplify:
    def __init__(self):
        self.tool=BaseReturn()
    def simplify_polynomial_equation(equation):
        """化简 n 元 n 次方程字符串。

        例如:
            simplify_polynomial_equation("x+2=3") == "x=3-2"
            simplify_polynomial_equation("xy+2xy+1=3") == "3xy=2"
        """

        # 分割等式为左右两部分
        left, right = equation.split("=")

        # 将左右两部分转换为多项式
        left_poly = {}
        right_poly = {}
        for term in left.split("+"):
            if term:
                coeff, var = term.split("*")
                left_poly[var] = left_poly.get(var, 0) + int(coeff)
        for term in right.split("+"):
            if term:
                coeff, var = term.split("*")
                right_poly[var] = right_poly.get(var, 0) + int(coeff)

        # 化简多项式
        simplified_left = ""
        simplified_right = ""
        for var, coeff in left_poly.items():
            if coeff == 1:
                simplified_left += var
            elif coeff == -1:
                simplified_left += "-" + var
            else:
                simplified_left += str(coeff) + var
        for var, coeff in right_poly.items():
            if coeff == 1:
                simplified_right += var
            elif coeff == -1:
                simplified_right += "-" + var
            else:
                simplified_right += str(coeff) + var

        # 返回化简后的等式字符串
        return simplified_left + "=" + simplified_right

if __name__=="__main__":
    s1=Simplify()
    print(s1.simplify_polynomial_equation("x+5=6"))