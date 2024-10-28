import json

with open('contacts.txt', 'r') as f:
    for line in f:
      ##Removes spaces at the beginning and end of the string
      p = f.read()
      contact = p.replace("\n", " ")
      print(contact)
      print()
      contact = contact.replace("} {", "},{")
      print("contact is "+str(contact))
      print()
      contact2 = {}
    #   print([element["name"][0]["name"] for element in contact])
      print(contact[contact.index("name")])
      ##Checks to see if the values inside are equal to the user input
      if "bork" == contact[contact.index("name")]:
       print(contact)
      elif "honk" == json.loads(contact):
          print("works with honk")
      else:
          print('user not found')
    # for line in f:
    #     contact = f.read()
    #     contact2 = [contact]
    #     print(contact)
    #     print(contact2)
    #     if contact2["name"] == "bork":
    #         print("Works")