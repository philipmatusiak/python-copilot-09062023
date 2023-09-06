# Tuple (single value, indexed, duplicates, values can not change)
myContacts = ("Philip", "Bob", "Joe", "Sally", "Joe")  # len tuple 4 indexed 0-3
print(myContacts)

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

