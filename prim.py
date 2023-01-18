# プリム法
# 全域木（全ての頂点が辺によって連結している木）の最小パターンを求める手法

import heapq # 優先度付きキュー（ヒープ木）モジュール

# 座標情報クラス
class State:
    # コンストラクタ
    def __init__(self, x, y, pre_x, pre_y, cost):
        self.x = x              # x座標
        self.y = y              # y座標
        self.pre_x = pre_x      # 1つ前のx座標
        self.pre_y = pre_y      # 1つ前のy座標
        self.cost = cost        # 2辺間のコスト
        
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

# プリム法
def prim(height, width, board, start_x, start_y):
    
    
    # 経過確認用
    cnt = 0
    
    # 未チェックのリスト
    unchecked_list = []
    # 未チェックリストを優先付きキューに変換
    heapq.heapify(unchecked_list)
    # チェック済み集合
    checked_set= set()
    # スタート情報のインスタンスを作成し、キューに入れる
    heapq.heappush(unchecked_list, State(start_x, start_y, start_x, start_y, 0))
    # 総コスト
    cost = 0
    
    # 未チェックがなくなるまで繰り返し
    while unchecked_list:
        # costが最小のものを取り出す
        st = heapq.heappop(unchecked_list)
        
        # すでにチェック済みの座標インスタンスだったらやり直し
        if st in checked_set:
            continue
        
        # チェック済み集合に追加
        checked_set.add(st)
        
        # 総コストに追加
        cost += st.cost
        
        # 経過確認用
        print(f"{cnt}回目")
        print(f"({st.pre_x},{st.pre_y})と({st.x},{st.y})を連結 総コスト{cost}")
        print("連結済み:",end="")
        for ch in checked_set:
            print(f"({ch.x},{ch.y})",end="")
        print()
        for i in range(height):
            for j in range(width):
                print((board[i][j]),end=" ")
            print()
        print("==================")

        # 全て連結し終わったら総コストを返して終了
        if len(checked_set) == width * height:
            return cost
        
        
        
        # 上下左右の座標を調べる
        for  dx, dy in [(st.x, st.y - 1), (st.x, st.y + 1), (st.x - 1, st.y), (st.x + 1, st.y)]:
            # boardの範囲内だったら
            if not (0 <= dx <= width - 1 and 0 <= dy <= height - 1):
                continue
            # costを計算
            dcost = board[st.y][st.x] * board[dy][dx]
            # 優先付きキューに追加
            heapq.heappush(unchecked_list, State(dx, dy, st.x, st.y, dcost))
            
        # 経過確認用カウント
        cnt += 1
    return -1


HEIGHT = 3 # 縦の長さ
WIDTH = 6 # 横の長さ

# 盤面
BOARD = [[0, 3, 1, 4, 1, 5],
         [9, 2, 6, 5, 3, 5],
         [3, 9, 7, 9, 3, 2]]

START_X,START_Y = 0, 0 # スタート座標(どの位置からでも同じ)

# ゴール到達時のインスタンス
cost = prim(HEIGHT, WIDTH, BOARD, START_X, START_Y)
# コストを出力
print(cost)