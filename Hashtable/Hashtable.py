hash_table = {}# Create an empty hash table (dictionary)
hash_table["apple"]=5
hash_table["banana"]=10
hash_table["cherry"]=7
# Retrieve values using keys
print("Value for 'apple':", hash_table['apple'])
print("Value for 'banana':", hash_table['banana'])
# Remove a key-value pair
if "cherry" in hash_table:
    del hash_table["cherry"]
else:
    print("Key not found")
