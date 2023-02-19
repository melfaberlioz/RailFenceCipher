# Rail Fence Cipher Encryption and Decryption

# function to ENCRYPT a message
def encryptRailFence(text, key):
    # create the matrix to cipher
    # plain text key = rows,
    # length(text) = columns
    # filling the rail matrix to distinguish filled spaces
    # from blank ones
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):

        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1

        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row += 1

    # construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("".join(result))


# This function receives cipher-text and key and returns the original
# text after decryption
def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

        # now we can construct the fill the rail matrix
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and
                        (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1

        # Now read the matrix in zigzag manner to construct the
        # resultant text
        result = []
        row, col = 0, 0
        for i in range(len(cipher)):

            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == key-1:
               dir_down = False

            # place the markers
            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1

            # find the next row using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
        return("".join(result))


# Driver code
if __name__ == "__main__":
    print(encryptRailFence("The rail fence cipher (also called a zigzag cipher)", 2))
    # print(encryptRailFence("In the rail fence cipher, the plaintext is written"
    #                        "downwards diagonally on successive 'rails' of an imaginary"
    #                        "fence, then moving up when the bottom rail is reached, down"
    #                        "again when the top rail is reached, and so on until the whole"
    #                        "plaintext is written out. The ciphertext is then read off in rows.", 5))
    # print(encryptRailFence("As we’ve seen earlier, the number of columns in rail fence cipher"
    #                        "remains equal to the length of plain-text message. And the key "
    #                        "corresponds to the number of rails.", 3))

    # Now decryption of the same cipher-text
