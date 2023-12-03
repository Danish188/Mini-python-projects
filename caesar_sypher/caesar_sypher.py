# try:
#     import paperclip
# except ImportError:
#     pass

# make string of all the Alphabets
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#information about the program
print('''
      The Caeser cipher encrypts letter by shifting them 
      over by a key number , for example a key of 2 means A
      is encrypted as C , the letter B is encrypted into D ,
      and so on.''')

# loop to ask the use to decrypt or encrypt the message
while True:
    print('''What do you want:
            (e)encrypt 
            (d)decrypt
          ''')
    
    response = input('> ')
    
    # defining the mode w.r.t to user choice entered
    if response.startswith("e"):
        mode = 'encrypt'
        break
    elif response.startswith("d"):
        mode = 'decrypt'
        break
    print("Please enter letter e or d!")
    
# loop to check the encryption/decryption criteria i-e 2 or 4    
while True:
    max_key = len(symbols)-1
    print('''Please enter the key from (0 - {})
             to encrypt or decrypt'''.format(max_key))
    response = input("> ")
    
    # if user did not enter the decimal return to response
    if not response.isdecimal():
        continue
    
    #else return the response into int and store it
    if 0 <= int(response) <= max_key:
        key = int(response)
        break

#get the message from user to encrypt or decrypt
print("Enter the message to {}".format(mode))
message = input('> ').upper()

translated = ''

#loop through the message
for symbol in message:
    # if character in symbols string 
    if symbol in symbols:
        # find the number of character
        num = symbols.find(symbol)
        #checking the mode
        if mode == 'encrypt':
            num = num + key # add the num to key
        elif mode == 'decrypt':
            num = num - key # subtract the num from key
        if num >= len(symbols): # if num is greater than len of symbols
            num = num - len(symbols)
        elif num < 0: # if numm is less than the len of symbols
            num = num + len(symbols)
        # concatenate the result
        translated = translated + symbols[num]
    else:
        translated = translated + symbol

print(translated)

# try:
#     paperclip.copy(translated)
#     print(f"Full {mode}ed text copied to clipboard")
# except:
#     pass     