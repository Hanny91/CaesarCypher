# Vignere cipher
message = list(input("Input your message: "))
alphabet = ("abcdefghijklmnopqrstuvwxyz")

operation_mode = input("Would you like to 'encode' or 'decode' a text?: ")


# Vignere Decoder
keyword = input('Word to decode by: ')
offset = []
for letter in keyword:
    if letter in alphabet:
        offset.append(alphabet.index(letter))
def vignere_cipher_decoder(message, offset):
    new_message = []
    offset_index = 0
    for letter in message:
        if letter in alphabet:
            current_offset = offset[offset_index]
            letter_offset = (alphabet.index(letter) + current_offset) % len(alphabet)
            new_message.append(alphabet[letter_offset])
            offset_index = (offset_index + 1) % len(offset)
        else:
            new_message.append(letter)
    return ("".join(new_message))

# Vignere Encoder
keyword = input('Word to encode by: ')
offset = []
for letter in keyword:
    if letter in alphabet:
        offset.append(alphabet.index(letter))
def vignere_cipher_encoder(message, offset):
    new_message = []
    offset_index = 0
    for letter in message:
        if letter in alphabet:
            current_offset = offset[offset_index]
            letter_offset = (alphabet.index(letter) - current_offset) % len(alphabet)
            new_message.append(alphabet[letter_offset])
            offset_index = (offset_index + 1) % len(offset)
        else:
            new_message.append(letter)
    return ("".join(new_message))

# Encoding and decoding modes
if operation_mode == "encode":
    keyword = int(input("Input the encoding keyword: "))
    print(vignere_cipher_encoder(message))

elif operation_mode == "decode":
    keyword = int(input("Input the decoding keyword: "))
    print(vignere_cipher_decoder(message))