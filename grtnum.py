a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
if a==b or a==c or a==d or b==c or b==d or c==d:
    print("error")
elif a>b and a>c and a>d:
    print("a is greater")
elif b>c and c>d:
    print("b is greater")
elif c>d:
    print("c is greater")
else:
    print("d is greater")
    