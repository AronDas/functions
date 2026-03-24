purchase_price = float(input("Please enter the purchase price:"))
amount_paid = float(input("Enter the amount Paid"))

change_due = amount_paid - purchase_price

if change_due < 0:
    print("You still owe: $", change_due)
elif change_due == 0:
    print("No change due")
else:
    print("Total change due: $", change_due)
