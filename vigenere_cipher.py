SPECIAL_CHARS = "() ,.-;:'_?!="
with open('question_3.txt', 'r') as file:
    message2 = file.read().replace('\n', '')
with open('question_3_decrypted.txt', 'r') as file:
    message3 = file.read().replace('\n', '')

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # this is the english letters


def encrypt(plain_text, key):
    cipher_text = ""
    kpos = []  # return the index of characters ex: if key='d' then kpos= 3
    i = 0

    for letter2 in key:
        kpos.append(alphabets.find(letter2))

    for letter3 in plain_text:
        if i == len(kpos):
            i = 0

        # If statement to remove any special characters defined above
        if letter3 in SPECIAL_CHARS:
            cipher_text += letter3
            continue
        if letter3.isdigit():
            cipher_text += letter3
            continue

        pos = alphabets.find(letter3.upper()) + kpos[i]
        if pos > 25:
            pos = pos-26
        cipher_text += alphabets[pos]
        i += 1


    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    kpos = []
    i = 0

    for letter2 in key:
        # Puts the key into the array kpos[]
        kpos.append(alphabets.find(letter2))
        # print(kpos) this is correct

    for letter3 in cipher_text:
        if i == len(kpos):
            i = 0
        # If statement to remove any special characters defined above
        if letter3 in SPECIAL_CHARS:
            plain_text += letter3
            continue
        if letter3.isdigit():
            plain_text += letter3
            continue
        pos = alphabets.find(letter3.upper()) - kpos[i]
        if pos < 0:
            pos = pos + 26
        plain_text += alphabets[pos]
        i += 1
    return plain_text


choose = 1
while choose == 1 or choose == 2 or choose == 4:
    print("You are using the Vigenere Cipher\n\nPress 1 to Enrypt a message \nPress 2 to Decrypt a message"
          "\nPress 3 to exit")
    key = 13
    choose = input("Choice: ")
    if choose == '1':
        plain_text = message3  # this will make sure that there is no space in the message

        cipher_text = encrypt(plain_text, key)
        print("The key used to decrypt this is: ", key)
        print("\nThe encrypted text is: \n", cipher_text)
        choose = 4

    elif choose == '2':
        cipher_text = message2

        plain_text = decrypt(cipher_text, key)
        print("The key used to decrypt this is: ", key)
        print("\nThe decrypted text is: \n", plain_text)
        choose = 4

if choose == '3':
    print("\n\t Thank you for using this service\n")

else:
    print("Please enter a valid choice!")
