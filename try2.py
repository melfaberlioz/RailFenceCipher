# Getting inputs from user. This will act
# as a plain text. Also, we need a key to encrypt our
# plain text. The key decides the number of rows in the grid.
s = input('Enter text: ')
k = int(input('Enter Key: '))

# Creating the grid. Use a blank list.
# The size of the list will be "key" * "length of the string".
# To initialize the list, we fill it with ' '(single space).

enc = [[" " for i in range(len(s))] for j in range(k)]
# used list comprehension (offers a shorter syntax when you want to
# create a new list based on the values of an existing list) for initializing
# the list. The size of the list is defined along with the value
# initialization.

# Putting characters into the grid.
# Defines a 'row' variable to determine which row to add our character to.
# Along with this, we also define a condition variable "flag" which
# determines whether we should travel in an upward or a downward direction.
# Initially, both row and flag will be 0.
flag = 0
row = 0

# To parse through all the characters in the plain text and determine its
# position in the grid.
# The character index will be the same as the column number in the grid.
# So we only need to deternime the row number. If flag=0, then we need to
# continue in the downward direction, if flag=1, then travel in an upward direnction.
# if flag=0, INCREMENT ROW NUMBER,
# if flag=1, DECREMENT ROW NUMBER.
# We also need a condition to change the value of flags. So if the row number of the
# current character is 0, the flag will be 0, and if the now number is Key-1 ie. the
# last row, the flag will be 1.
for i in range(len(s)):
    enc[row][i] = s[i]
    if row == 0:
        flag = 0
    elif row == k-1:
        flag = 1
    if flag == 0:
        row += 1
    else:
        row -= 1

# Printing grid
# We have filled our plaintext characters into grid. Let's check if
# they are in the right position.
# For this we use the join() function which will convert out list to
# a string.
# JOIN() method takes all items in an iterable and joins them into one string.
for i in range(k):
    print("".join(enc[i]))

# Getting ChipherText:
# For getting the chiphertext, we need to read out our grid row by row
# and eliminate the spaces between each letter in a row.
# To do this, we will parse through each character in every row and append
# all the character, which are not spaces, to an initial empty list.
ct = []
for i in range(k):
    for j in range(len(s)):
        if enc[i][j] != ' ':
            ct.append(enc[i][j])

# Convert 'ct' list to string and get ciphertext
cipher = "".join(ct)
print('Cipher Text: ', cipher)


dec = [['' for i in range(len(cipher))] for j in range(k)]

row = 0
flag = 0

for i in range(len(cipher)):
    if row == 0:
        flag = 0
    if row == k - 1:
        flag = 1

    dec[row][flag] = '*'
    flag += 1

    if flag:
        row += 1
    else:
        row -= 1

    index = 0
    for i in range(k):
        for j in range(len(cipher)):
            if ((dec[i][j] == '*') and
                    (index < len(cipher))):
                dec[i][j] = cipher[index]
                index += 1

    result = []
    row = 0
    flag = 0
    for i in range(len(cipher)):
        # check the direction of flow
        if row == 0:
            flag = 0
        if row == k - 1:
            flag = 1

        # place the markers
        if dec[row][flag] != '*':
             result.append(dec[row][flag])
             flag += 1

        # find the next row using direction flag
        if flag:
            row += 1
        else:
            row -= 1
    print("".join(result))


if __name__ == "__main__":
    print(dec)

