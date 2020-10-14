n = input().split()
n1 = int(n[0])
l1 = []
l3 = []

for _ in range(n1):
    m = input().split()
    l1.append(m)

for i in l1:
    l2 = list(map(int, i))
    l3.append(l2)

x = int(input())

def takeIndex(e):
    return e[x]

for i in l3:
    l3.sort(key=takeIndex)

for l in l3:
    print(*l, sep=' ')







