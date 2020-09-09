from __future__ import division

n, bag = map(int, input().split(" "))
totalLootValue = 0
lootValue = [0] * n
lootWeight = [0] * n
valuePair = [0] * n

for entry in range(0, n):
    a, b = map(int, input().split(" "))
    lootValue[entry], lootWeight[entry] = a, b
    valuePair[entry] = lootValue[entry] / lootWeight[entry]

while (True):
    if (bag != 0):
        entry = max(valuePair)
        i = valuePair.index(entry)
        w = lootWeight[i]
        r = min(bag, w)
        bag -= r
        lootWeight[i] -= r
        totalLootValue += r * valuePair[i]
        if (lootWeight[i] == 0):
            lootValue[i] = 0
            valuePair[i] = 0
    else:
        break

print(totalLootValue)