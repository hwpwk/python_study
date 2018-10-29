
class Person(object):
    def __init__(self, name):# この初期化したものをコンストラクタと呼ぶ
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run'* num)
# person.say_something()オブジェクトが使われなくなった時点でdef __del__(self)が呼び出される
    def __del__(self):
        print('good bye')

person = Person('Tom')
person.say_something()
