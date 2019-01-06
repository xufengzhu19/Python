#a=b=c=1
#a,b,c=1,'2',3.0
#print(a)
#print(b)
#print(c)



#不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
#可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
########################################################################
#============Number
#Python3 支持 int、float、bool、complex（复数）。
#isinstance 和 type 的区别在于：
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
#class A:
#    pass
#class B(A):
#    pass
#print(isinstance(A(),A))#True
#print(type(A())==A)#True
#print(isinstance(B(),A))#True
#print(type(B())==A)#False
########################################################################
#数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数，向下取整。
#//也不一定是整数，与分子分母类型有关
#在混合计算时，Python会把整型转换成为浮点数。
#print(10/2)#5.0
#print(10//2)#5
#print(10//(3/2))#6.0
########################################################################
#a=1
#b=2
#print(a>b)
########################################################################
#============String
#1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
#2、字符串可以用+运算符连接在一起，用*运算符重复。
#3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
#4、Python中的字符串不能改变。
#str='123456'
#print (str)          # 输出字符串
#print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
#print (str[0])       # 输出字符串第一个字符
#print (str[2:5])     # 输出从第三个开始到第五个的字符
#print (str[2:])      # 输出从第三个开始的后的所有字符
#print (str * 2)      # 输出字符串两次
#print (str + "TEST") # 连接字符串
#123456
#12345
#1
#345
#3456
#123456123456
#123456TEST
########################################################################
#print('abc\nno')
#print(r'abc\nno')
#abc
#no
#abc\nno
########################################################################
#a='2344'
#print(a.join('nnn'))#n2344n2344n
#print(a.join('n'))#n
#print(a.startswith('2'))#True
#str='dfdfds2324dDDLNdnkd; '
#print(str.capitalize())#Dfdfds2324dddlndnkd ;
#print(str.count('2'))#2
#print(str.split('2'))#['dfdfds', '3', '4dDDLNdnkd; ']
#print(str.strip())#dfdfds2324dDDLNdnkd;
#print(str.find('d'))#0
#print(str.index('2'))#6
########################################################################
#============List
#有序的对象集合，支持嵌套
#list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
#tinylist = [123, 'runoob']
#print (list)            # 输出完整列表
#print (list[0])         # 输出列表第一个元素
#print (list[1:3])       # 从第二个开始输出到第三个元素
#print (list[2:])        # 输出从第三个元素开始的所有元素
#print (tinylist * 2)    # 输出两次列表
#print (list + tinylist) # 连接列表
#['abcd', 786, 2.23, 'runoob', 70.2]
#abcd
#[786, 2.23]
#[2.23, 'runoob', 70.2]
#[123, 'runoob', 123, 'runoob']
#['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
#l=list[:]
#ll=list
#print(l)#['abcd', 786, 2.23, 'runoob', 70.2]
#print(list==l)#True
#print(l is list)#False
#print(ll is list)#True
########################################################################
#list=['a','b','c']
#list.append('d')
#print(list)
#del list[3]
#print(list)
#list+=['d']
#print(list)#['a', 'b', 'c', 'd']
#a=(1,2,3)
#b=list(a)
#print(b)#[1, 2, 3]
#print(list.count('a'))
#print(list.pop())#c
#print(len(list))#2
#list.remove('a')
#print(len(list))#1
#print(list.index('c'))#2
#list.reverse()
#print(list)#['c', 'b', 'a']
#b=list.copy()
#print(b)#['a', 'b', 'c']
#print(b==list)#True
#print(b is list)#False'
# 获取列表的第二个元素
#def takeSecond(elem):
#    return elem[1]
## 列表
#random = [(2, 2), (3, 4), (4, 1), (1, 3)]
## 指定第二个元素排序
#random.sort(key=takeSecond)
## 输出类别
#print ('排序列表：', random)#[(4, 1), (2, 2), (1, 3), (3, 4)]
########################################################################
#============Tuple
#构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
#tup1 = ()    # 空元组
#tup2 = (20,) # 一个元素，需要在元素后添加逗号
#print(tup1[0])
#tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
#或t='abcd', 786 , 2.23, 'runoob', 70.2
#tinytuple = (123, 'runoob')
#print (tuple)             # 输出完整元组
#print (tuple[0])          # 输出元组的第一个元素
#print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
#print (tuple[2:])         # 输出从第三个元素开始的所有元素
#print (tinytuple * 2)     # 输出两次元组
#print (tuple + tinytuple) # 连接元组
#('abcd', 786, 2.23, 'runoob', 70.2)
#abcd
#(786, 2.23)
#(2.23, 'runoob', 70.2)
#(123, 'runoob', 123, 'runoob')
#('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')
########################################################################
#string、list和tuple都属于sequence（序列）。
#l=[1,2,3]
#print(tuple(l))#(1, 2, 3)
########################################################################
#============Set
#基本功能是进行成员关系测试和删除重复元素。
#可以使用大括号 { } 或者 set() 函数创建集合
#注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
#s={'a','b',2,3,'c','a',2}
#print(s)#{2, 3, 'a', 'c', 'b'}
#if 'a' in s:
#    print(True)
#True
#ss={'a',3,4}
#print(s-ss)#{'c', 2, 'b'}
#print(s|ss)#{2, 3, 'a', 4, 'c', 'b'}
#print(s&ss)#{3, 'a'}
#print(s^ss)#{2, 4, 'c', 'b'}
########################################################################
#============Dictionary
#它是一个无序的 键(key) : 值(value) 的集合。
#键(key)必须使用不可变类型，且唯一
#dic={'a':1,'b':2,3:3}
#print(dic)#{'a': 1, 'b': 2, 3: 3}
#print(dic['a'])#1
#print(dic.keys())#dict_keys(['a', 'b', 3])
#print(type(dic.keys()))#<class 'dict_keys'>
#print(dic.items())#dict_items([('a', 1), ('b', 2), (3, 3)])
#print(dic.values())#dict_values([1, 2, 3])
#print(dic.get(0))#None
#print(dic.get('a'))#1
########################################################################
#构造函数 dict() 可以直接从键值对序列中构建字典如下：
#print(dict([('Runoob', 1), ('Google', 2), ('Taobao'#, 3)]))
#{'Runoob': 1, 'Google': 2, 'Taobao': 3}
#print({x:x**2 for x in [2,4,6]})
#{2: 4, 4: 16, 6: 36}
#print(dict(1=a,2=b))
#SyntaxError: keyword can't be an expression
#print(dict(a=1,b=2))
#{'a': 1, 'b': 2}


#斐波纳契数列
#a, b = 0, 1
#while b < 10:
#    print(b, end=',')
#    a, b = b, a+b
#1,1,2,3,5,8,
########################################################################
#for a in 'adggfg':
#    if a=='f':
#        pass
#    else:
#        raise StopIteration
########################################################################
#l=[1,2,3,4]
#it=iter(l)
#print(next(it))
#for x in it:
#    print(x)
#import sys
#while True:
#    try:
#        print (next(it))
#    StopIteration 异常用于标识迭代的完成
#    except StopIteration:
#        sys.exit()
########################################################################
#函数可以作为结果，返回值，参数等
#def gener(num):
#    print("start!")
#    while num<10:
#        num+=1
#        yield num
#        print("after yield")
#for i in gener(0):
#    print("i="+str(i))
#start!
#i=1
#after yield
#i=2
#after yield                
########################################################################
#sum=lambda a,b:a+b
#print(sum(1,2))
#n=1
#def fun1():
#    n+=1
#    print(n)
#fun1()
#print(n)
#UnboundLocalError: local variable 'n' referenced before assignment
#def fun2():
#    global n
#    n+=1
#    print("n="+str(n))#n=2
#fun2()
#print(n)#2
########################################################################   
#def outer():
#    num=1
#    def inner():
#        nonlocal num
#        num+=1
#        print("inner_num="+str(num))#inner_num=2
#        return num
#    inner()
#    print(num)#2
#f=outer.inner()
#print(f())
########################################################################
#l=[2,4,6]        
#ll=[[x,x**2] for x in l]
#print(ll)
#[[2, 4], [4, 16], [6, 36]]
#将列表推导式的[]改成()即可得到生成器。
#multiples = (i for i in range(30) if i % 3 is 0)
#print(type(multiples))
#<class 'generator'>
#快速更换key和value
#mcase = {'a': 10, 'b': 34}
#mcase_frequency = {v: k for k, v in mcase.items()}
#print(mcase_frequency)
#{10: 'a', 34: 'b'}
#squared = {x**2 for x in [1, 1, 2]}
#print(squared)
#{1, 4}
########################################################################
#python的pickle模块实现了基本的数据序列和反序列化。
#通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
#通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
#pickle.dump(obj, file, [,protocol])
#x = pickle.load(file)
########################################################################
#while True:
#    try:
#        x = int(input("Please enter a number: "))
#        break
#    except ValueError:
#        print("Oops!  That was no valid number.  Try again   ")
########################################################################
#self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类
#elf 不是 python 关键字，我们把他换成 this,abc.. 也是可以正常执行
#在类的内部，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
#class Test:
#    def prt(self):
#        print(self)
#        print(self.__class__)
#t = Test()
#t.prt()
#<__main__.Test object at 0x0000002B0EFBAA90>
#<class '__main__.Test'>
########################################################################
#Python同样有限的支持多继承形式。多继承的类定义形如下例:
#class DerivedClassName(Base1, Base2, Base3):
#class Parent:        # 定义父类
#   def myMethod(self):
#      print ('调用父类方法')
# 
#class Child(Parent): # 定义子类
#   def myMethod(self):
#      print ('调用子类方法')
# 
#c = Child()          # 子类实例
#c.myMethod()         # 子类调用重写方法
#super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
#调用子类方法
#调用父类方法


