# Allows the user to code and decode text using a Caesar Cipher
# Shifts each of the letters in the message along the alphabet
# Codes and decodes given an offset, or brute forces an unknown offset.

operation_mode = input("Would you like to 'encode', 'decode' or 'brute force' a text?: ")
message = list(input("Input your message: "))
alphabet = ("abcdefghijklmnopqrstuvwxyz")

# Decodes by shifting letters backwards in the alphabet.
def ceasar_cypher_decoder(message, offset):
    new_message = []
    for letter in message:
        if letter in alphabet:
            letter_offset = (alphabet.index(letter) - offset)
            if letter_offset >= 0:
                new_message.append(alphabet[letter_offset])
            else:
                new_message.append(alphabet[letter_offset + 26])
        else:
            new_message.append(letter)
    return ("".join(new_message))

# Encodes by shifting letters forward in the alphabet
def ceasar_cypher_encoder(message, offset):
        new_message = []
        for letter in message:
            if letter in alphabet:
                letter_offset = alphabet.index(letter)+ offset
                if letter_offset < 26:
                    letter_replaced = alphabet[letter_offset]
                    new_message.append(letter_replaced)
                else:
                    letter_replaced = alphabet[letter_offset % 26]
                    new_message.append(letter_replaced)
            else:
                new_message.append(letter)
        return ("".join(new_message))

# Encoding and decoding modes
if operation_mode == "encode":
    offset = int(input("Input the required offset: "))
    print(ceasar_cypher_encoder(message))

elif operation_mode == "decode":
    offset = int(input("Input the required offset: "))
    print(ceasar_cypher_decoder(message))
    

# Brute forces the code by testing each possible offset 
else:
    offset = 1
    def brute_force(message):
        bruted_message = ceasar_cypher_decoder(message, offset)
        return bruted_message
    print(brute_force(message))
    solved_question = input("Enter 'Y' if it looks like words: ")

    # Asks the user to check for correct decoding
    while solved_question != "Y":
        offset += 1
        print(offset)
        print(brute_force(message))
        solved_question = input("Does it look like words? 'Y' or 'N': ")

