card_valid = input("insert the card? ")
pin = int(input("enter your pin: "))
amount = int(input("enter amount "))
if card_valid == "yes" and pin == 1234 and amount <=1500 and amount%100 == 0:
    print("you have withdrawn the amount")
else:
    print("invalid")    