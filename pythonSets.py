# Sets (single value, not indexed, unordered, values can not change, duplicates are not allowed)
myContacts = {"Philip", "Bob", "Joe", "Sally", "Joe"}  # len set 4
print(myContacts)
print(len(myContacts))  #4

# for loop
# for x in ys
# x is the local variable in the loop
# ys is the data source
print("Contacts")
print("--------")
i = 0  #row identifier for an instance of time
for fname in myContacts:
    #print("Contact first name: " + fname) # string function
    print("Contact id:", i, "Contact first name:", fname)   # parameter function
    i = i+1

myContactsList = list(myContacts)
print(myContactsList)