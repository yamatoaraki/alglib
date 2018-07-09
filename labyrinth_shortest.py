# coding=utf-8
"""
def debug_print(maze):
    for xx in maze:
        for yy in xx:
            print yy,
        print "\n",
"""
def clear_maze(sx, sy, gx, gy, maze):

    #debug_print(maze)

    INF = 100000000

    field_x_length = len(maze)#Row
    field_y_length = len(maze[0])#Colum
    distance = [[INF for i in range(field_x_length)] for j in range(field_y_length)]
    #    distance = [[None]*field_x_length]*field_y_length
    #print(distance)
    def bfs():
        queue = []

        queue.insert(0, (sx, sy))
        print(queue)
        distance[sx][sy] = 0

        while len(queue):
            x, y = queue.pop()
            if x == gx and y == gy:
                break

            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

                if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and maze[nx][ny] != '#' and distance[nx][ny] == INF):
                    queue.insert(0, (nx, ny))
                    #print(queue)
                    distance[nx][ny] = distance[x][y] + 1

        print(distance)
        return distance[gx][gy]

    return bfs()

def shortest_pass(sx,sy,gx,gy,maze):
    INF = 100000000

    field_x_length = len(maze)#Row
    field_y_length = len(maze[0])#Colum
    distance = [[INF for i in range(field_x_length)] for j in range(field_y_length)]
    q = [[sx,sy]]
    while len(q) > 0:
        path = q.pop(0)
        n = path[len(path)-1]
        print(path)
        if n!=1:
            x = n[0]
            y = n[1]
        else:
            x = path[0]
            y = path[1]
        if x == gx and y == gy:
            #print(path)
            break
        else:
            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and maze[nx][ny] != '#' and distance[nx][ny] == INF):
                    new_path = path[:]
                    new_path = [new_path]
                    new_path.append([nx,ny])
                    distance[nx][ny] = distance[x][y] + 1
                    q.append(new_path)



maze = [
    ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
    ]

sx, sy = 0, 1 # スタート地点の座標
gx, gy = 9, 8 # ゴール地点の座標
#print (clear_maze(sx, sy, gx, gy, maze))
shortest_pass(sx,sy,gx,gy,maze)
