# Creating a dictionary
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Accessing values using keys
print(my_dict["key1"])  # Output: value1

# Adding new key-value pairs
my_dict["new_key"] = "new_value"

# Modifying values
my_dict["key2"] = "updated_value"

# Removing key-value pairs
del my_dict["key3"]

# Iterating through a dictionary
for key, value in my_dict.items():
    print(key, "->", value)


"""Get Usage"""

a = {
    1:"Jan",
    2:"Feb"
}

print (a.get(2,"is the Month")) #Result will be displayed
print (a.get(3,"is the Month"))  #Result Not Displayed it shows only the Print
print (a.get(2)) #Result Not Displayed