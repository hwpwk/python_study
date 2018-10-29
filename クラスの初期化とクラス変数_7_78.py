class Person(object):
    def __init__(self):# classの初期設定 この関数内で初期設定をいろいろと設定できる
        print('First')

    def say_something(self):
        print('hello')

person = Person()# 1つ下のperson.say_something()がなくてもdef__init__(self)を実行できる
person.say_something()
#####################################################
#####################################################
# Personというオブジェクトに値を保持させたいときselfの後に引数を設定
# クラスはselfがないと値を保持できないので値を保持したい場合はselfをつける必要あり
class Person(object):
    def __init__(self, name):
        self.name = name# self(自分自身)のnameに引数を入れる
        print(self.name)

    def say_something(self):
        print('hello')

person = Person('Tom')# 1つ下のperson.say_something()がなくてもdef__init__(self)を実行できる
# person.say_something()
#####################################################
#####################################################
# def __init__(self, name)でself.nameとしたので他のメソッドからも呼び出すことが可能
class Person(object):
    def __init__(self, name):
        self.name = name# self(自分自身)のnameに引数を入れる

    def say_something(self):
        print('I am {}. hello'.format(self.name))

person = Person('Tom')# 1つ下のperson.say_something()がなくてもdef__init__(self)を実行できる
person.say_something()
