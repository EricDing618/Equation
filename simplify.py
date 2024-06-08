import re

def simplify_equation_string(equation):
  """化简n元n次方程字符串。

  Args:
    equation: 要化简的方程字符串。

  Returns:
    化简后的方程字符串。
  """

  # 分离等号两边
  left, right = equation.split("=")

  # 去除两边的空格
  left = left.strip()
  right = right.strip()

  # 将等号两边的字符串拆分为项
  left_terms = re.split(r"(\+|-)", left)
  right_terms = re.split(r"(\+|-)", right)

  # 分别处理等号两边的项
  simplified_left = simplify_terms(left_terms)
  simplified_right = simplify_terms(right_terms)

  # 合并化简后的项
  simplified_equation = f"{simplified_left}={simplified_right}"

  # 返回化简后的方程字符串
  return simplified_equation


def simplify_terms(terms):
  """化简一个列表中的项。

  Args:
    terms: 要化简的项列表。

  Returns:
    化简后的项字符串。
  """

  # 创建一个字典来存储项和系数
  term_dict = {}

  # 遍历项
  for term in terms:
    # 如果项是一个数字，则将系数添加到常数项中
    if term.isdigit():
      term_dict[""] = term_dict.get("", 0) + int(term)
    # 如果项是一个变量，则将系数添加到变量项中
    else:
      term_dict[term] = term_dict.get(term, 0) + 1

  # 将项和系数重新排列成一个字符串
  simplified_terms = ""
  for term, coefficient in sorted(term_dict.items()):
    if coefficient == 0:
      continue
    if coefficient == 1:
      simplified_terms += term
    else:
      simplified_terms += f"{coefficient}{term}"

    if simplified_terms and term != "":
      simplified_terms += " + "

  # 返回化简后的项字符串
  return simplified_terms.rstrip(" + ")


simplified_equation = simplify_equation_string("x+2=3")
print(simplified_equation)