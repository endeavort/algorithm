# 上に1つずらしたとき
def up(dice):
    f, u, d, b = dice[0], dice[2], dice[3], dice[1]
    dice[0] = d
    dice[2] = f
    dice[3] = b
    dice[1] = u
    return dice

# 下に1つずらしたとき
def down(dice):
    f, u, d, b = dice[0], dice[2], dice[3], dice[1]
    dice[0] = u
    dice[2] = b
    dice[3] = f
    dice[1] = d
    return dice

# 左に1つずらしたとき
def left(dice):
    f, l, r, b = dice[0], dice[5], dice[4], dice[1]
    dice[0] = r
    dice[5] = f
    dice[4] = b
    dice[1] = l
    return dice

# 右に1つずらしたとき
def right(dice):
    f, l, r, b = dice[0], dice[5], dice[4], dice[1]
    dice[0] = l
    dice[5] = b
    dice[4] = f
    dice[1] = r
    return dice

# 展開図を表示
def show(dice):
    print(" ", dice[2], " ")
    print(dice[5], dice[0], dice[4], dice[1])
    print(" ", dice[3], " ")
    print()

# サイコロの初期状態
#    2
#  4 1 3 6
#    5
dice = [1, 6, 2, 5, 3, 4]
# 正面, 裏, 上, 下, 右, 左

show(dice)
dice = up(dice)
show(dice)
dice = down(dice)
show(dice)
dice = left(dice)
show(dice)
dice = right(dice)
show(dice)