
# deal.py 发牌
import random

def gen_pocker(n):
    # 进行n次随机交换，模拟洗牌过程
    for _ in range(n):
        idx1 = random.randint(0, 51)
        idx2 = random.randint(0, 51)
        pocker[idx1], pocker[idx2] = pocker[idx2], pocker[idx1]

def getColor(card):
    # 根据牌的编号获取花色
    colors = ['梅花', '方块', '红桃', '黑桃']
    return colors[card // 13]

def getValue(card):
    # 根据牌的编号获取数值
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return values[card % 13]

def getPuk(card):
    return f"{getColor(card)}{getValue(card)}"

pocker = list(range(52))

gen_pocker(100)

players = [[] for _ in range(4)]

for _ in range(13):
    for player in players:
        card = pocker.pop(0)
        player.append(getPuk(card))

for i, player in enumerate(players):
    print(f"玩家 {i+1} 的牌:")
    print(player)
