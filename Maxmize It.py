a, b = map(int, input().split())
l = []
s = []
for _ in range(a):
    c = list(map(int, input().split()))
    l.append(c)
for i in l:
    i.sort()
    print(i[-1])
    s.append((i[-1]))
sum = 0
for res in s:
    sum += res ** 2
print(sum % b)






