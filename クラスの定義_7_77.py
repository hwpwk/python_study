# クラスに(object)とつけるのはpython2系の書き方
# python3系の場合は()がなくても大丈夫
# Personというオブジェクトを作ってこの人が何か言う(say_something)メソッドというように簡単に作れるのがクラス
class Person(object):
    def say_something(self):
        print('hello')

# Personクラスを呼び出しオブジェクトを作成
person = Person()
person.say_something()# 「hello」が表示される
