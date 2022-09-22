x = int(input("enter tomato price: "))
if x > 50 :
    result = x + (20/100) * x
    print("tomato price: ", result)
if x < 50 :
    result = x + (40/100) * x
    print("tomato price: ", result)