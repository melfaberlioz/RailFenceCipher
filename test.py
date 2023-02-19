def main():
    text = input('Input Text : ')
    key = int(input('Input Key : '))

    while True:
        choice = input('Encrypt or Decrypt (0/1)')
        if choice in ['0', '1']:
            break

    if int(choice):
        enc = [['' for i in range(len(text))] for j in range(key)]

        # dir_down = None
        row = 0
        flag = 0

        for i in range(len(text)):
            enc[row][i] = text[i]
            if row == 0:
                flag = 0
            elif row == key - 1:
                flag = 1
            if flag == 0:
                row += 1
            else:
                row -= 1

            # enc[row][flag] = ''
            # flag += 1
            # if dir_down:
            #     row += 1
            # else:
            #     row -= 1

        # print('')
        # [print(row) for row in arr]
        # count = 0
        # for row in arr:
        #     for i in range(len(row)):
        #         if row[i] == '':
        #             row[i] = text[count]
        #             count += 1
        for i in range(key):
            print("".join(enc[i]))
        # print('')
        # [print(row) for row in arr]

        ct = []
        # row, col = 0, 0
        # for i in range(len(text)):
        for i in range(key):
            for j in range(len(text)):

             if row == 0:
                flag = 0
             if row == key - 1:
                flag = 1

                if enc[row][flag] != '':
                    ct.append(enc[row][flag])
                    flag += 1

            if flag == 0:
                row += 1
            else:
                row -= 1

        # print(result)
    else:
        enc = [[] for j in range(key)]
        count = 0
        finish = False

        while True:
            for j in range(0, key - 1):
                enc[j].append(text[count])
                count += 1

                if count >= len(text):
                    finish = True
                    break

            if finish:
                break

            for k in range(key - 1, 0, -1):
                enc[k].append(text[count])
                count += 1

                if count >= len(text):
                    finish = True
                    break

            if finish:
                break
        print(enc)


if __name__ == '__main__':
    main()
