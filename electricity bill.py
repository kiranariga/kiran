a = int(input("enter number of units: "))
if a<=100:
    print("no charge")
elif a>100 and a<=150:
    result = (a-100)*4
    print("bill is:", result)
elif a>150:
    result = (a-150)*10 + (50*4)
    print("bill is:", result)