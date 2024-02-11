a=int(input("a的值"))
b=int(input("b的值"))
c=int(input("c的值"))
d=b**2-4*a*c
if d<0:
    print("方程无解")
elif d==0:
    print("方程有一个解")
else:
    print("方程有两个解")