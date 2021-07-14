#王者荣耀每一场对战都有10位玩家参与，假设每位玩家都有一个实力值。
#我们需要把这些玩家分成两组，为了尽可能让双方实力平衡，请你输出这两组的最小实力差。
power = [1,5,1,1,1,1,1,1,1,1]
total = 0
for i in power:
    total = total + i
a = 0
for i in range(5):
    a = a + power[i]
b = total - a
ans = abs(a - b)
for i in range(10):
    for j in range(i,10):
        for k in range(j,10):
            for h in range(k,10):
                for m in range(h,10):
                    partA = power[i] +power[j] + power[k] + power[h] + power[m]
                    partB = total - partA
                    cha =abs( partA - partB)
                    if(cha < ans):
                        ans = cha
print(ans)


