a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
elif a==c and c>b:
    print("A and C are equal")
elif a==b and b>c:
    print("A and B are equal")
elif b==c and b>a:
    print("B and C are equal")
else:
    print("They are equal")