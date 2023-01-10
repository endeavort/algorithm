# リストをキュートして使うときは、dequeを使った方が処理が早くなる
# それを確認するための実験コード

import time # timeモジュールのインポート
 
strat = time.time() # プログラムの開始時刻

# pop(0)を利用した場合
#==================================================
# 1から100000までのリスト
num_list = list(range(1,100001))

total = 0

while len(num_list) > 0:
    total += num_list.pop(0)
#==================================================
 
end = time.time() # プログラムの終了時刻
runTime = end - strat # 処理時間
 
print(f"pop(0):{runTime}") # 処理時間を表示

from collections import deque # dequeモジュールのインポート

strat = time.time() # プログラムの開始時刻

# dequeを利用した場合
#==================================================
# 1から100000までのリスト
num_list = deque(range(1,100001))

total = 0

while len(num_list) > 0:
    total += num_list.popleft()
#==================================================

end = time.time() # プログラムの終了時刻
runTime = end - strat # 処理時間

print(f"deque:{runTime}") # 処理時間を表示