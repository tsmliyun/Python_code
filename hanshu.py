# 函数的demo

var1 = 112
def func():
    global var1
    var1 = 222
    print(var1)

# 调用函数
func()
print(var1)
