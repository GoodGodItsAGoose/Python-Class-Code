price = 100
discount = 0.2
is_member = False
items_sold = "50"
message = "Total items sold: " + items_sold
if is_member == False:
    final_price = price
    print("Final Price:", final_price)
    print(message)
    print("Membership discount was not applied. You are not a member.")
elif is_member == True:
    final_price = price * discount
    print("Final Price:", final_price)
    print(message)
    print("Membership discount applied: ", str(discount))