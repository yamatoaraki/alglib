#スペースで区切られた１行を受けとる。
#n,m,s = map(int,input().split())

#文字の区切り方
test = "orange,apple,banana,strawberry"
print(test.split(","))#→['orange', 'apple', 'banana', 'strawberry']

#文字列の置換
src = "aaabbbccc"
dst = src.replace("b","B")
print(dst)#→aaaBBBccc
#置換先文字列のを空文字にすると削除される
dst = src.replace("b","")
print(dst)#→aaaccc
#複数の文字列を置換
dst = src.replace("a","A").replace("b","B").replace("c","C")
print(dst)#→AAABBBCCC
s = 'one two one two one'
print(s.translate(str.maketrans({'o': 'O', 't': 'T'})))
# One TwO One TwO One
print(s.translate(str.maketrans({'o': 'XXX', 't': None})))
# XXXne wXXX XXXne wXXX XXXne
#正規表現で置換するパターン
import re
s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'
#第一引数に正規表現パターン、第二引数に置換先文字列、第三引数に処理対象の文字列を指定する。
print(re.sub('[a-z]*@', 'ABC@', s))
# ABC@xxx.com ABC@yyy.com ABC@zzz.com
#正規表現について。大括弧[]で囲むとその中の任意の一文字にマッチする。
print(re.sub('[xyz]', '1', s))
# aaa@111.com bbb@111.com ccc@111.com
#パターンの一部を()で囲むと、置換先文字列の中で()で囲んだ部分にマッチする文字列を使用することができる。
print(re.sub('([a-z]*)@', r'\1-123@', s))
# aaa-123@xxx.com bbb-123@yyy.com ccc-123@zzz.com
#パターンを|で区切るといずれかのパターンにマッチする。
print(re.sub('aaa|bbb|ccc', 'ABC', s))
# ABC@xxx.com ABC@yyy.com ABC@zzz.com
#置換した部分の個数を取得
t = re.subn('[a-z]*@', 'ABC@', s)
print(t)
# ('ABC@xxx.com ABC@yyy.com ABC@zzz.com', 3)
print(type(t))
# <class 'tuple'>
print(t[0])
# ABC@xxx.com ABC@yyy.com ABC@zzz.com
print(t[1])
# 3

#文字列のスライス
l = [0, 10, 20, 30, 40, 50, 60]
print(l[2:5])
# [20, 30, 40]
#startを省略すると最初からstopを省略すると最後まで。
#両方を省略すると全ての値が選択される
print(l[:3])
# [0, 10, 20]
print(l[3:])
# [30, 40, 50, 60]
print(l[:])
# [0, 10, 20, 30, 40, 50, 60]
#増分stepも可能
print(l[::2])
# [0, 20, 40, 60]
#スライスによる値の代入
l[2:5] = [200, 300, 400]
print(l)
# [0, 10, 200, 300, 400, 50, 60]
#注意！！！！要素としてリストなどを含んでいる複合オブジェクトの場合は、リストの要素を更新すると元のオブジェクトも変更される。
l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
l_2d_slice = l_2d[1:3]
print(l_2d_slice)
# [[3, 4, 5], [6, 7, 8]]
l_2d_slice[0][1] = 400
print(l_2d_slice)
# [[3, 400, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 400, 5], [6, 7, 8], [9, 10, 11]]
#これを防ぐためには標準ライブラリのcopyモジュールをインポートし、deepcopy()を使う。
import copy
l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
l_2d_slice_deepcopy = copy.deepcopy(l_2d[1:3])
print(l_2d_slice_deepcopy)
# [[3, 4, 5], [6, 7, 8]]
l_2d_slice_deepcopy[0][1] = 400
print(l_2d_slice_deepcopy)
# [[3, 400, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
