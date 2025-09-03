p = int(input("Enter loan total: "))
n = int(input("Enter total months: "))
R = int(input("Enter interest: "))

r = R/(12*100)
EMI = p * r * ((1+r)**n)/((1+r)**n-1)
for number in range(1,n):
    balance = p-EMI
    print("EMI:", EMI)
    print("Balance:", balance)
    print("------")
