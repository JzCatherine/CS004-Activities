lsymbols = """`~!@#$%^&*()-_=+"""
rsymbols = """{}[]|\\;:'",<.>/?"""
special_symbols = lsymbols + rsymbols
numbers = "1234567890"
valid_symbols = "abcdefghijklmnopqrstuvwxyz " + numbers + special_symbols

#scans and validates character of the inputted string
#only those symbols that are matched inside the global variable will be replaced
#unmatched symbols will be ignored and removed
def check(paragraph):

    validated_text = ""

    for char in paragraph:
        if char in valid_symbols:
            validated_text += char
    return validated_text

# KEYWORD ======================================
def original(password):

    keyword = ""

    for char in password:
        if char in valid_symbols:
            if char not in keyword:
                keyword += char

    for char in valid_symbols:
        if char not in keyword:
            keyword += char

    return keyword

# KEYWORD-Reverse ======================================
def Reverse1(password):

    keyword = ""
    password = password
    reverseString = "".join(reversed(password))

    for char in reverseString:
        if char in valid_symbols:
            if char not in keyword:
                keyword += char

    for char in valid_symbols:
        if char not in keyword:
            keyword += char

    return keyword

# KEYWORD-Atbash ======================================
def Keyword_Atbash(password):
    origKey = ""
    keyword = ""

    for char in password:
        if char in valid_symbols:
            if char not in origKey:
                origKey += char

    for char in valid_symbols:
        if char not in origKey:
            origKey += char

    keyword = "".join(reversed(origKey))
    
    return keyword

# KEYWORD-Keyletter ======================================
def Keyletter(password, keyletter):
    
    position = valid_symbols.find(keyletter)
    
    keyword = original(password)
    print("Position>", position, "|| PASSWORD>",password, " || keyletter>", keyletter)
    print("1KEYWORD>>", keyword)
    keyword = keyword[-position:] + keyword[:-position] 
    print("2KEYWORD>>", keyword)
    return keyword


# ENCRYPTION =================================================================================
def encrypt(validated_text, keyword):
    cipher_text = ""
    index_values = [valid_symbols.index(char) for char in validated_text]
    cipher_text ="".join(keyword[indexKeyword] for indexKeyword in index_values)
    
    return cipher_text
# DECRYPTION =================================================================================
def decrypt(cipher_text, keyword):
    deciphered_text = ""
    index_values = [keyword.index(char) for char in cipher_text]
    deciphered_text = "".join(valid_symbols[indexKeyword] for indexKeyword in index_values)

    return deciphered_text

def display(result):
    print("\t" + result)

def switch(variation, password):
    keyletter = ""
    if variation == 4:
        keyletter = input("\nEnter keyletter: ").lower()
    dict={
        1: original(password),
        2: Reverse1(password),
        3: Keyword_Atbash(password),
        4: Keyletter(password, keyletter)
    }
    return dict.get(variation, 'Invalid Operation')  

def main():

    choice = int(input('\n[1] Encyrpt\n[2] Decrypt\nEnter Choice: '))

    if choice == 1:
        user_input = input("\nEnter Message to Encrypt: \n").lower()
        user_key = input("\nEnter Encrypting Keyword: ").lower()

        print('\nPress 1 for Original\nPress 2 for Reverse Keyword Variation\nPress 3 for Keyword-Atbash Cipher\nPress 4 for Keyword-Keyletter Cipher\n')
        selection = int(input("Select Keyword Cipher Variation: "))

        valid = check(user_input)
        variant = switch(selection, user_key)
        print(variant)
        encrypted = encrypt(valid, variant)

        print("\nCiphered Text → \n")
        display(encrypted)

    if choice == 2:
        user_input = input("\nEnter or Paste Cipher Text to Decrypt: \n").lower()
        user_key = input("\nEnter Decryption Key: ").lower()

        print('\nPress 1 for Original\nPress 2 for Reverse Keyword Variation\nPress 3 for Keyword-Atbash Cipher\nPress 4 for Keyword-Keyletter Cipher\n')
        selection = int(input("Select Keyword Cipher Variation: "))

        variant = switch(selection, user_key)
        decrypted = decrypt(user_input, variant)

        print("\nDeciphered Text → \n")
        display(decrypted)

if __name__ == "__main__":
    main()