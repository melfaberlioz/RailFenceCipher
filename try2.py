# Getting inputs from user. This will act
# as a plain text. Also, we need a key to encrypt our
# plain text. The key decides the number of rows in the grid.
s = input('Enter string: ')
k = int(input('Enter Key: '))

# Creating the grid. Use a blank list.
# The size of the list will be "key" * "length of the string".
# To initialize the list, we fill it with ' '(single space).

enc = [[" " for i in range(len(s))] for j in range(k)]
print(enc)