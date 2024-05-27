#數字與字串兩類變數的宣告
x=11
y=22
a="13"
b="14"
print("x+y=",x+y)
print("a+b=",a+b)

#List添加、查詢元素
a_list=[1,2,3,4]
print(a_list[:])
a_list.append(5)
print(a_list[:])
#List更新、刪除元素
print("first num is",a_list[0])
a_list[0]=8
print("first num becomes",a_list[0])
del a_list[0]
print(a_list[:])