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
    # 未チェックのリスト
    unchecked_list = []
    # 未チェックリストを優先付きキューに変換
    heapq.heapify(unchecked_list)
    # チェック済み集合
    checked_set= set()
    # スタート情報のインスタンスを作成し、キューに入れる
    heapq.heappush(unchecked_list, State(start_x, start_y, board[start_y][start_x]))
    
    while unchecked_list:
        st = heapq.heappop(unchecked_list)