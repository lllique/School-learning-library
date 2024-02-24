#定义一个函数
def func1(param1,param2,param3=1):
    r1 = param1 + param2
    r2 = param2 + param3
    r3 = param3 + param1
    r4 = param1 +param2 +param3
    return r1,r2,r3,r4
#各种调用方式
A,B,C,D = func1(3,2) #第三个参数会使用默认值
A,_,_,_ = func1(3,2) #如果只需要第一个返回值
print('A:',A)

All = func1(param2=2,param1=3)#显式填写参数可以改变参数顺序
print('All:',All,type(All))#tuple类型
print('All[0]:',All[0])





