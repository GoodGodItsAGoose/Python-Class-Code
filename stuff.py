# default args

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.10))

import time

# default args must be at the end of the arguments
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)

    print("DONE!")

# count(30, 15)

# keyword arguments = preceeded by an identifier, helps with readability, order of args doesnt matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
# positinal args first, then keywords
# hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")
# for x in range(1, 11):
#     print(x, end=" ")
# print("1", "2", "3", sep = "-")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=206, first=334, last=1682)

# print(phone_num)

# *args (arguments), allows to pass multiple
# *kwards (keyword arguments), allows to pass multiple
# usually args, but can be other
# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2,3,4,5,6,7,8,9))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("john", "eerie", "thomas", "doe")

# def address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# address(street="154 Deepend Street", city="Plagus", state="CA", zip="99810")
def shipping_label(*args, **kwargs):
    for arg in args:
       print(arg, end = " ")
    print()
    for value in kwargs.values():
       print(value, end = " ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('appt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('direction')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr", "Lagos", "Perskine", "Jones",
               street="154 Deepend St", direction="SW", city="Plagus", state="CA", zip="99810")
