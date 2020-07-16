# 这是一个集合的demo

bri = set(['bra', 'rus', 'ind'])

bri.add('test')
print(bri)

print('bra' in bri)

bric = bri.copy()

bric.add('china')

print(bric)

print(bric.issuperset(bri))

bri.remove('rus')

print(bri)
