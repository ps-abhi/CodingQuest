t = int(input())

while t > 0:
    n, x = map(int, input().split())
    # Your code goes here
    num=str(n*x)
    if num[0]!= 0 and len(num)==5:
        print("YES")
    else:
        print("NO")
    t -= 1
