from collections import deque # dequeモジュールのインポート

# 座標情報クラス
class State:
    # コンストラクタ
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # ハッシュ値の設定:インスタンス同士の比較演算をする際に必要
    def __hash__(self):
        # self.x を16ビット左にシフトさせたものと self.y の論理和をハッシュ値に設定
        return (self.x << 16) | self.y

    # インスタンスを「==」で比較したときに呼び出される
    # ※　今回は「in」を利用するとき
    def __eq__(self, other):
        # self.x と self.y の値が同じだったら True を返す
        return self.x == other.x and self.y == other.y

# 幅優先探索：Breadth-First Search
def bfs(height, width, maze, start_x, start_y, goal_x, goal_y):
    # スタート情報のインスタンスを作成し、キューに入れる
    que = deque([State(start_x, start_y)])
    # チェック済み集合
    checked= set()
    # 通ったマスの数
    cost = 1
    
    while True:
        # 一時的なキュー
        tmp_que = deque()
        # 同じ距離のマスを全て調べる
        while que:
            # 次の探索座標インスタンスをキューから取り出す
            st = que.popleft() 
            # ゴール座標だったらcostの値を返す
            if st.x == goal_x and st.y == goal_y:
                return cost
            # 壁だったらやり直し
            if maze[st.y][st.x] == "#":
                continue
            # すでにチェック済みの座標インスタンスだったらやり直し
            if st in checked:
                continue
            
            # チェック済み集合に追加
            checked.add(st)
            
            #     上  下  左  右 の座標用コマンド
            dx = [ 0, 0, -1, 1]
            dy = [-1, 1,  0, 0]
            for i in range(4):
                nx = st.x + dx[i]
                ny = st.y + dy[i]
                
                # 迷路範囲外だったらやり直し
                if not (0 <= nx <= width - 1 and 0 <= ny <= height - 1):
                    continue
                # １歩進んだマスをキューに追加
                tmp_que.append(State(nx, ny))
                
        # 同じ距離のマスを全て調べ終わったら、1歩増えたキューを探索対象にする
        que = tmp_que
        cost += 1

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
# スタート座標
START_X = 1
START_Y = 1
# ゴール座標
GOAL_X = 10
GOAL_Y = 10 

cost = bfs(HEIGHT, WIDTH, board, START_X, START_Y, GOAL_X, GOAL_Y)
print(cost)