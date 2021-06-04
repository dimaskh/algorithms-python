data = [22, 40, 102, 105, 23, 31, 6, 5]
hash_table = [None] * 15
tblLen = len(hash_table)

def hash_function(value, table_size):
  return value % table_size

for value in data:
  hash_table[hash_function(value, tblLen)] = value

print(hash_table)
