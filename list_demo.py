# 这是一个list demo

shopList = ['apple', 'mango', 'carrot', 'banana']

print(len(shopList))

print('I have ', len(shopList), ' items to purchase')

for item in shopList:
    print(item, end=' ')

print('I have also buy rice')

shopList.append('rice')
print('My shopping list is now', shopList)

print('I will sort my list now')
shopList.sort()
print('My shopping list is now', shopList)

print('the first item i will buy is', shopList[0])
olditem = shopList[0]
del shopList[0]
print('i bought the', olditem)
print('My shopping list is now', shopList)

shopList.insert(1, 'red')
print('My shopping list is now', shopList)

shopList.pop()
print('My shopping list is now', shopList)


# help(list)
