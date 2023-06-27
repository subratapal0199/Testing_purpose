n=15
a=0
b=1
print("Fibonacci Series:", a, b, end=" ")
for i in range(2,15):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
print()