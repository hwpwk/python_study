
class Person(object):
    def __init__(self, name):
        self.name = name# self(自分自身)のnameに引数を入れる

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run'* num)

person = Person('Tom')
person.say_something()
