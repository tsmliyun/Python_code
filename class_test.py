class Player():
    def __init__(self, name, hp):
        self.__name = name
        self.hp = hp

    def print_role(self):
        print('%s:%s' % (self.__name, self.hp))

    def updateName(self, name):
        self.__name = name


user1 = Player('tom', 100)
# user2 = Player('jem', 200)

user1.updateName('hhh')
# user1.name = 'aaa'
user1.print_role()

# user2.print_role()

print('user1的类型 %s' % type(user1))
