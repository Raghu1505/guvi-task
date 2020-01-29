rows = int(input("Enter the number of rows : "))
for i in range(0, rows):
    a = 1

    for j in range(1, rows-i):
        print("  ", end="")
    
    for k in range(0, i+1):
        print("  ", a, end="")
        a = int(a * (i - k) / (k + 1))

    print()
