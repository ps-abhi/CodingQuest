# cook your dish here
for i in range(int(input())):
    x, y = map(int, input().split())
    if x<y:
        while not(x>=y):
            x=x*2
    else:
        while not(y>=x):
            y=y*2
    if x==y:
        print("YES")
    else:
        print("NO")
        