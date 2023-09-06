# Lists (single value, indexed, duplicates, values can change)
myContacts = ["Philip", "Bob", "Joe", "Sally"]  # len list 4 indexed 0-3
print(myContacts)

# access a list element by the the index #
print(myContacts[1]) # Bob

#check to see if the contact exists
if "Bob" in myContacts:
    print("Bob is a customer")
else:
    print("Bob is not a customer")

# for loop
# for x in ys
# x is the local variable in the loop
# ys is the data source
print("Contacts")
print("--------")
i = 0
for fname in myContacts:
    #print("Contact first name: " + fname) # string function
    print("Contact id:", i, "Contact first name:", fname)   # parameter function
    i = i+1

contactid = int(input("Enter the contact id to change: "))
myContacts[contactid] = input("Enter an updated name for " + myContacts[contactid] + ": ")
print(myContacts)
