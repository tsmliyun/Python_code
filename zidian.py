# 这是一个字典demo

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print(ab.get('Swaroop'))

print("swaroop's address is ", ab['Swaroop'])

ab['test'] = 'test'
print(ab)

ab.pop('Larry')
print(ab)

del ab['Spammer']
print(ab)
# print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))



d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
print(d1)

s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1)