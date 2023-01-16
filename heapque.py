import heapq # 優先度付きキュー（ヒープ木）モジュール
# ヒープ木：根が最小値、または最大値となるように構成された木構造
# heapqを利用すると、リストが最小から最大に整列されるため、計算量が減る

# 座標情報クラス
class State:
    # コンストラクタ
    def __init__(self, x, y, cost):
        self.x = x # x座標
        self.y = y # y座標
        self.cost = cost # コスト
        
    # ハッシュ値の設定:インスタンス同士の比較演算をする際に必要
    def __hash__(self):
        # self.x を16ビット左にシフトさせたものとself.yの論理和をハッシュ値に設定
        return (self.x << 16) | self.y

    # インスタンスを「==」で比較したときに呼び出される
    # ※今回は「in」を利用するとき
    def __eq__(self, other):
        # 他のインスタンスのself.xとself.yの値が同じだったらTrueを返す
        return self.x == other.x and self.y == other.y
    
    # インスタンスを「<,>」で比較したときに呼び出される
    # ※今回はヒープ木に挿入するとき
    def __lt__(self, other):
        # 他のインスタンスのself.costよりも小さかったらTrueを返す
        return self.cost < other.cost

# ダイクストラ法
def dijkstra(height, width, board, start_x, start_y, goal_x, goal_y):
    
    # # 経過確認用のリスト
    # progress_list = [[0] * width for _ in range(height)]
    
    # 未チェックのリスト
    unchecked_list = []
    # 未チェックリストを優先付きキューに変換
    heapq.heapify(unchecked_list)
    # チェック済み集合
    checked_set= set()
    # スタート情報のインスタンスを作成し、キューに入れる
    heapq.heappush(unchecked_list, State(start_x, start_y, board[start_y][start_x]))
    cnt = 0
    # 未チェックがなくなるまで繰り返し
    while unchecked_list:
        # costが最小のものを取り出す
        st = heapq.heappop(unchecked_list)
        
        # ゴール座標だったらcostの値を返して終了 
        if st.x == goal_x and st.y == goal_y:
            return st.cost
        
        # すでにチェック済みの座標インスタンスだったらやり直し
        if st in checked_set:
            continue
        
        # チェック済み集合に追加
        checked_set.add(st)
        
        # # 経過確認用
        # print(f"{cnt}回目")
        # print(f"x座標:{st.x} y座標:{st.y} コスト{st.cost}")
        # progress_list[st.y][st.x] = st.cost
        # for i in range(height):
        #     for j in range(width):
        #         if j == width -1:
        #             print(str(progress_list[i][j]).center(2))
        #         else:
        #             print(str(progress_list[i][j]).center(2),end=" ")
        # print("==================")
        
        # 上下左右の座標を調べる
        for  dx, dy in [(st.x, st.y - 1), (st.x, st.y + 1), (st.x - 1, st.y), (st.x + 1, st.y)]:
            # boardの範囲内だったら
            if not (0 <= dx <= width - 1 and 0 <= dy <= height - 1):
                continue
            # costを計算
            dcost = st.cost + board[dy][dx]
            # 優先付きキューに追加
            heapq.heappush(unchecked_list, State(dx, dy, dcost))
        cnt += 1
    return -1
                
# 左上のスタートから右下のゴールまで移動するときに
# 通るマス (スタート、ゴール含む) のコストの合計の最小値を求めよ

HEIGHT = 3
WIDTH = 6
BOARD = [[0, 3, 1, 4, 1, 5],
         [9, 2, 6, 5, 3, 5],
         [3, 9, 7, 9, 3, 2]]

START_X,START_Y = 0, 0
GOAL_X,GOAL_Y = WIDTH - 1, HEIGHT - 1

ans = dijkstra(HEIGHT, WIDTH, BOARD, START_X, START_Y, GOAL_X, GOAL_Y)
print(ans)