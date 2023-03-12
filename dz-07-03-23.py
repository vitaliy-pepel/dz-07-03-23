#task30
n = int(input())
x = int(input())
y = int(input())
for i in range(y):
    print(n + i * x)
    
#task32
listt = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minn = int(input())
maxx = int(input())
for i in range(len(listt)):
    if minn <= listt[i] <= maxx:
        print(i)