#lake_countingはDFSで池を潰していく
#左上から走破する。

def lake_counting(field):

    field_x_length = len(field) #Row 横

    field_y_length = len(field[0])　#Colum 縦


    lake_count = 0

    def dfs(x,y):
        field[x][y] = '.'
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and field[nx][ny] == 'W'):
                    dfs(nx, ny)
    def dfs_4(x,y):
        field[x][y] = '.'
        dx_4 = [0,1,0,-1]
        dy_4 = [1,0,-1,0]
        for i in range(4):
            nx = x + dx_4[i]
            ny = y + dy_4[i]
            if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and field[nx][ny] == 'W'):
                dfs_4(nx,ny)

    for i in range (0, field_x_length):
        for j in range (0, field_y_length):
            if (field[i][j] == 'W'):
                dfs(i, j)　　#8方向バージョン
                #dfs_4(i,j) #4方向バージョン
                lake_count+=1

    return lake_count

#fieldの作り方
#h, w = map(int, input().split())　#縦＊横
#matrix = [list(map(int, input().split())) for _ in range(h)]#fieldが数字で表されている場合
#matrix = [list(map(str, input().split())) for _ in range(h)]#fieldが文字列で表されている場合

field = [
    ['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
    ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ]

print (lake_counting(field))
