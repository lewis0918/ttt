my_list=[1,2,3,4,5]

# 用for loop操作List
for item in my_list:
    print(item)

# 用for loop搭配if else，對list內的元素作判斷
for item in my_list:
    if item > 3:
        print(item)
    else:
        print("Less than or equal to 3")

# 沒有帶參數的python def
def my_function_no_params():
    print("This is a function without parameters")

# 有帶參數的python def
def my_function_with_params(param1, param2):
    print("Parameter 1:", param1)
    print("Parameter 2:", param2)

# 沒有帶參數，但有帶return的python def
def my_function_no_params_with_return():
    return "This is a function without parameters but with return"

# 有帶參數，有帶return的python def
def my_function_with_params_and_return(param1, param2):
    return param1 + param2

# 測試以上定義的函數
my_function_no_params()
my_function_with_params("Hello", "World")
print(my_function_no_params_with_return())
print(my_function_with_params_and_return(3, 5))