import math
import cmath
import mpmath

'''复数的加减法示例'''
print('复数的加减法示例')
x1 = a = complex(2, 4)
print(x1, x1.real, x1.imag, x1.conjugate()) # (2+4j) 2.0 4.0 (2-4j)
x2 = 1.5e-7j  # 00000015j
print(x2, abs(x2), type(x2)) #1.5e-07j 1.5e-07 <class 'complex'>
x3 = 1 + 2j
print(x3)
x1 += x2
print(x1)
x1 += x3

'''math、cmath和mpmath'''
print('math、cmath和mpmath库效果对比')
print(math.sqrt(3))#1.7320508075688772
print(cmath.sqrt(3))#(1.7320508075688772+0j)
print(mpmath.sqrt(mpmath.mpf(3))) #1.73205080756888
# print(math.sqrt(-1))#会报错
print(cmath.sqrt(-1)) #1j
print(mpmath.sqrt(-1)) #(0.0 + 1.0j)

'''print格式化输出的例子'''
print ("姓名:%s 年龄:%d 身高:%.3f" % ("张三",25,1.83))

'''等待键盘输入，并显示的例子'''
a = input("输入一个数字：") #注意实际接收的是字符串
#print("a+1=：",a+1)#会报错，因为a是字符串
print("a+1=：",int(a)+1) #如果a不能转换为字符串也会报错