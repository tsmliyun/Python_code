import time


# print(time.time())

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("运行时间 %s 秒" % (end_time - start_time))

    return wrapper


# 装饰器
@timer
def i_can_sleep():
    time.sleep(3)


#
# start_time = time.time()
# print(start_time)
i_can_sleep()
# end_time = time.time()
# print(end_time)
