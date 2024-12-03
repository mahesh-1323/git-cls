n=int(input())
md=n%10
while n!=0:
    d=n%10
    if d>md:
        md=d
    n=n//10
print(md)