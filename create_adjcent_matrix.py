############この関数はノードとエッジが与えられた場合のみ使える###########
n = int(input())
#nはノード数
p = []
#このループ回数はエッジの数だけループするように変更する
for i in range(n-1):
    p.append(list(map(int, input().split())))
#p=[[3, 6], [1, 2], [3, 1], [7, 4], [5, 7], [1, 4]]
#pは上のようなエッジのリスト。３と６をつなぐ、１と２をつなぐ・・・
print(p)
def create_matrix(p):
    m =[ [0]*n for i in range(n)]
    for path in p:
        m[path[0]][path[1]] = 1
        m[path[1]][path[0]] = 1
    print(m)

create_matrix(p)
