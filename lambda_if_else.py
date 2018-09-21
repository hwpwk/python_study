# 引数が3未満ならば2を掛け、3以上ならば3で割って5で足す関数

def func1(x):
    if x < 3:
        return X*2
    else:
        return x / 3 + 5

print(func1(3))

# 上記関数はlamdbaを使うと1行で表現可能
# 条件を満たす時の処理 if 条件 else 条件を満たさない時の処理
# つまり、lambda (引数) : (条件を満たす時の処理) if (条件) else (条件を満たさない時の処理)
(lambda x:x*2 if x<3 else x/3 +5)(3)
print((lambda x:x*2 if x<3 else x/3 +5)(3))# 出力:6.0