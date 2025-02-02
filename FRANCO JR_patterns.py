num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()
i = 1

while i <= num:
    j = 1
    while j <= i:
        print(i, end="")
        j+=1
    print()
    i+=1