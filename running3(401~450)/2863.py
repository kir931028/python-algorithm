a, b = map(int, input().split())
c, d = map(int, input().split())
ls = [a/c+b/d, c/d+a/b, d/b+c/a, b/a+d/c]
print(ls.index(max(ls)))