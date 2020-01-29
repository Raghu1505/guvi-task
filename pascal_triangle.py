a = [1]
b = [0]
n = int(input("Enter the size: "))
for i in range(n):
        print(a)
        a = [j+k for j,k in zip(a+b, b+a)]
