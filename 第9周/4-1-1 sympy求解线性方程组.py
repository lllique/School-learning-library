import sympy as sp

x1, x2, x3 = sp.symbols('x1 x2 x3')

# 例子1：
result = sp.solve([x1 - 2 * x2 + 3 * x3 - 1,
                   2 * x1 + 3 * x2 + x3 - 2,
                   3 * x1 - x2 - x3 - 4],
                  [x1, x2, x3])
print(result, type(result))  # 输出类型为字典类型

# 例子2：
result = sp.solve([x1 + x2 - 21 / 50 - 1, -x1 - 6 * x2 + 3 / 25], [x1, x2])
print(result)

#例子3：解一元高次方程
#result = sp.solve([x1 ** 2 +7 * x1 + 6 ], [x1])
result = sp.solve([x1 ** 3 +7 * x1 ** 2 + 16 * x1 +12 ], [x1])
print(result)

#例子4：sympy的roots方法（求特征根）
print(sp.roots(x1 ** 3 +7 * x1 ** 2 + 16 * x1 +12,x1))
