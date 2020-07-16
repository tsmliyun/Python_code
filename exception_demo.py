# 这是一个异常演示demo

# try:
#     text = input('Enter something -->')
# except EOFError:
#     print('why did you do an eof on me')
# except KeyboardInterrupt:
#     print('you cancelled the operation')
# else:
#     print('you entered {}'.format(text))

# i = j

# d = {'a':1,'b':2}
#
# print(d['c'])

# year = int(input('input year:'))



# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('请输入数字')

# a = 123
# a.append()

# except (ValueError,AttributeError,KeyError)
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('0不能做除数')


# try:
#     print(1/'a')
# except Exception as e:
#     print(' %s' %e)


# try:
#    raise NameError('Hello Error')
# except NameError:
#     print('my customer error')

# try:
#     a = open('name.txt')
# except Exception as e:
#     print(e)
# finally:
#     a.close()

# if name is not None
#     print(name)

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))


print('continue')








