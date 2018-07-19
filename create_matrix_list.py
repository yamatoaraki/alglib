n,m = map(int, input().split())
list1 = []
def create_list_matrix(n,m):
    for i in range(n):
        a = input()
        b = list(a)
        list1.append(b)
create_list_matrix(n,m)
print(list1)
'''
8 5
RRRRR
RRRRR
RRRRR
RRRRR
RRRRR
RRRRR
RRRRR
RRRRR
'''
#上のような入力を下のようなリストにする関数
'''
[['R', 'R', 'R', 'R', 'R'],
 ['R', 'R', 'R', 'R', 'R'],
 ['R', 'R', 'R', 'R', 'R'],
 ['R', 'R', 'R', 'R', 'R'],
 ['R', 'R', 'R', 'R', 'R'],
 ['R', 'R', 'R', 'R', 'R'],
 ['R', 'R', 'R', 'R', 'R'],
 ['R', 'R', 'R', 'R', 'R']]
'''
