############この関数はノードとエッジが与えられた場合のみ使える###########
#入力例
#7　←ノード数
#3 6　これ以下はエッジ
#1 2
#3 1
#7 4
#5 7
#1 4
n = int(input
#nはノード数
p = []
#このループ回数はエッジの数だけループするように変更する
for i in range(n-1):
    p.append(list(map(int, input().split())))
#p=[[3, 6], [1, 2], [3, 1], [7, 4], [5, 7], [1, 4]]
#pは上のようなエッジのリスト。３と６をつなぐ、１と２をつなぐ・・・

#この関数はノードの数nとエッジのリストを引数にとる。
def create_adjcect_list(n,p):
    l = [[] for i in range(n+1)]
    for pi in p:  #0-originedに注意
        l[pi[0]].append(pi[1])
        l[pi[1]].append(pi[0])
    l.pop(0)#リストの先頭削除
    print(l)
create_adjcect_list(n,p)
