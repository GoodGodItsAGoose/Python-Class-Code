#The origional flawed code is as follows:
price = "100" #The price should be a integer
discount = 0.2
final_price = price * (1-discount) #The discount should only apply if the customer is a member.
items_sold = 50
message = "Total items sold: " + items_sold #You can't add an integer to a string variable
is_member = False
member_discount = is_member * 0.1 #You cannot do math with a boolean variable, it is logically incorrect.
print("Final price: ", final_price)
print(message)
print("Membership discount applied: ", member_discount) #The discount should only count if the customer is a member.

#the variables with incorrect data types:
price = "100" #This should be an integer so it can be used later on
items_sold = 50 #This should be a string so it can be combined with 'message'

#incorrect mixing of strings
message = "Total items sold: " + items_sold #As said before, integers can't be mixed with strings.

#incorrect math equations
is_member = False
member_discount = is_member * 0.1 #multiplying a boolean by an integer will not work.

#executing operations that shouldn't be executed unless certain requirements are met
final_price = price * (1-discount) #this should only happen if the customer is a member.
print("Membership discount applied: ", member_discount) #This will change if the customer is not a member.
print("Final price: ", final_price) #the final price will change depending on whether the customer is a member.



price = 100 #I made this an integer so it can be used later to calculate the final price
discount = 0.2
is_member = False
items_sold = "50" #Made this a string so it can be mixed with the string in message
message = "Total items sold: " + items_sold
#added this so if the customer is a member, it will apply the discount, but if not, it will not apply the discount
if is_member == False:
    final_price = price
    print("Final Price:", final_price)
    print(message)
    print("Membership discount was not applied. You are not a member.")
elif is_member == True:
    final_price = price * discount #I dont think the discount is meant to be subtracted by 1, and if so, the discount could just be set to 0.8.
    print("Final Price:", final_price)
    print(message)
    print("Membership discount applied: ", str(discount))
