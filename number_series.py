n=int(input("Enter a number"))
a=0
b=1
print(a)
print(b)
for i in range(n):
        sum=a+b
        a=b
        b=sum
        print(sum)
