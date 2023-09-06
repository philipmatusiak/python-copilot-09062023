# Dictionary (key: value, indexed key(!duplicate), values (duplicate), values can change)

myContact = {
    "fname": "Philip",
    "lname": "Matusiak",
    "age": 21, # 3?
    "numberOfOrders": 21,
    "allOrdersShipped": True
}
print(myContact)

print("Contact Full Name:", myContact["fname"], myContact["lname"])

newAge = int(input("Enter new age for contact: "))
myContact.update({"age": newAge})
print(myContact)

