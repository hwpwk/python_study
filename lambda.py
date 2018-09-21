# def,,,と関数を定義した後すぐにreturn,,,と返り値を返すような関数を作成したい場合
# lambdaを使うことで関数を1行にまとめることが可能
# lambda式の構造は lambda (引数): (返り値)

def test_func(x):
    return x**2

test_func2 =lambda x:x**2

# 作成関数が実行されるか確認
# lambdaを使用した場合も変数に()をつけて関数のように扱うことができる
print(test_func(3)) # 出力:9
print(test_func2(3)) # 出力:9

# lambda式で多変数の関数を作成したい場合
addition = lambda x, y:x + y
print(addition(1,3)) # 出力:4


# lambdaは変数に格納しなくても使用可能
(lambda x:x**2)(3)
print((lambda x:x**2)(3)) # 出力:9
