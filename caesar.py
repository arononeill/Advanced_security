ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARS = " ,.-;:_?!="
counter = 0


def encrypt(plain_text, key):

    # Encrypts the parameter plain text using the key and returns the ciphered text
    cipher_text = ""
    for letter in plain_text:
        # If statement to remove any special characters defined above
        if letter in SPECIAL_CHARS:
            cipher_text += letter
            continue
        index = ALPHABET.find(letter.upper())
        number = index + key
        new_index = number - (26*(number//26))
        cipher_text += ALPHABET[new_index]
    return cipher_text


def decrypt(cipher_text, key):

    # Decrypts the parameter cipher text using the key and returns the now decryped plain text.
    plain_text = ""
    for letter in cipher_text:
        # If statement to remove any special characters defined above
        if letter in SPECIAL_CHARS:
            plain_text += letter
            continue
        index = ALPHABET.find(letter.upper())
        number = index + key
        new_index = number - (26*(number//26))
        plain_text += ALPHABET[new_index]
    print("\nThe decrypted message")
    return plain_text


def key(plaintext, key):

    while key < 26:
        plain_text = decrypt(plaintext, key)
        print("using the key : " + str(key))
        print(plain_text)
        key += 1


def key2(plaintext, key):

    while key < 26:
        plain_text = encrypt(plaintext, key)
        print("using the key : " + str(key))
        print(plain_text)
        key += 1


with open('question_1.txt', 'r') as file:
    message1 = file.read().replace('\n', '')
with open('question_2.txt', 'r') as file:
    message2 = file.read().replace('\n', '')
with open('question_6.txt', 'r') as file:
    message3 = file.read().replace('\n', '')


def question(question_choice):
    if question_choice == 1:
        message = message1
    elif question_choice == 2:
        message = message2
    elif question_choice == 6:
        message = message3
    else:
        print("ERROR")
    return message


def encryption_choice(counter):
    if counter == 0:
        print('Do you have a key \n Press 1 for key \n Press 2 for no key')
        key_choice = int(input(""))
        if key_choice == 1:
            print('Please enter the key')
            key = int(input(""))
            print("\nThe encrypted message is:\n")
            print(encrypt(message, key))
            counter = 1

        if key_choice == 2:
            print(key2(message, 0))
            counter = 1
        return counter

    else:
        return


def decryption_choice(counter):
    if counter == 0:
        print('Do you have a key \n Press 1 for key \n Press 2 for no key')
        key_choice = int(input(""))
        if key_choice == 1:
            print('Please enter the key')
            key2 = int(input(""))
            print(decrypt(message, key2))
            counter = 1

        if key_choice == 2:
            print(key(message, 0))
            counter = 1

        return counter

    else:
        return


question_choice = int(input("Press 1 for Question 1 OR \n Press 2 for Question 2 OR \n Press 6 for Question 6 \n Press 3 to exit at any time\n"))
while question_choice == 1 or question_choice == 2 or question_choice == 6:
    counter = 0
    user_input = 3
    message = question(question_choice)
    print('\nThis machine has 2 functions: \n Press 1 for encryption \n Press 2 for decryption \n Press 5 to exit')
    user_input = int(input("Enter choice:"))

    while user_input != 5 and user_input != 4:
        if user_input == 1:
            counter = encryption_choice(counter)
            question_choice = 1
            user_input = 4

        if user_input == 2:
            counter = decryption_choice(counter)
            question_choice = 2
            user_input = 4

    if user_input == 5:
        question_choice = 3


if question_choice == 3:
    print("\n\t Thank you for using this service\n")

else:
    print("\nPlease enter a valid entry")
