# Convert text to binary ASCII code:
    # 1. Get character from the string
    # 2. Get decimal code of character from the ASCII table
    # 3. Convert the ASCII decimal value of the character to binary byte
    # 4. Continue with next character, and repeat the proces until all the characters from the string is converted.

def strToBinaryASCII(string):
    # binary_output list will contain the Binary ASCII code converted from the text string input
    binary_output = []
    # loop the process of converting the ASCII decimal value of the character from the string to binary byte, 
    # until all the characters from the string is converted.
    for c in string:
        # ord() function: Character to ASCII value
        ascii_val = ord(c)
         
        # bin() function: ASCII value to binary
        binary_val = bin(ascii_val)
        # add the current binary value to binary_output list
        binary_output.append(binary_val[2:])
    
    # Dsiplay the Binary Output 
    print("\nASCII Binary Output: ")
    print(' '.join(binary_output))

# Get the string message input from the user

print("B I N A R Y  E N C O D I N G\n")
string = input("Enter Message: ")
# Driver code to call the function strToBinaryASCII(), 
# the string variable is passed as a parameter to the function
strToBinaryASCII(string)


print('\n')