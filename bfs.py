# 幅優先探索：Breadth-First Search
# 近いところから順に全て探索する

from collections import deque # dequeモジュールのインポート
from copy import deepcopy # コピーモジュールのインポート

# 迷路
MAZE = ["############",
        "#S#..#.....#",
        "#..#...#.###",
        "##.#.###.#.#",
        "##.#..##.#.#",
        "##.##.##...#",
        "#.....##.###",
        "######...#.#",
        "##.....#...#",
        "##.#.##.####",
        "#..#......G#",
        "############"]

# mazeを2次元リスト化
board = [list(line) for line in MAZE]

HEIGHT = 12 # 縦の長さ
WIDTH = 12 # 横の長さ
START = (1, 1) # スタート座標
GOAL = (10, 10) # ゴール座標

# boardリストのコピー
maze = deepcopy(board)

# スタートからの距離の2次元リスト（探索前は-1)
distance = [[-1] * WIDTH for _ in range(HEIGHT)]
distance[START[0]][START[1]] = 0

# スタート座標をキューに入れる
que = deque([START])

# キューの要素がなくなるまで繰り返し
while que:
    # 次の探索座標をキューから取り出す
    y, x = que.popleft() 
    
    # 距離の書き込み（スタート地点を除く）
    if not maze[y][x] == "S": 
        maze[y][x] = str(distance[y][x])
    
    # ゴール座標だったら終了
    if y == GOAL[0] and x == GOAL[1]: 
            break
    
    # 上下左右の座標を調べる
    for  dy, dx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]: 
        if maze[dy][dx] == '.': # もし通路だったら
                que.append((dy,dx)) # キューに追加
                distance[dy][dx] = distance[y][x] + 1 # 距離のリストを更新

# 探索データを出力
for line in maze:
    for l in line:
        print(l.center(3), end='') # 見やすくするため,3文字範囲の中心揃えで出力
    print()