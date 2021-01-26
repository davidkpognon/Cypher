# *******************************************************
# CSCI-121 Elements of Computer Programming II
# Caesar Cypher
# *******************************************************

import string

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}


def encrypt(message, key):
    encrypted_message = ''
    for ch in message:
        if ch in ordinal_value:
            shifted_value = (ordinal_value[ch]+key) % len(alphabet)
            encrypted_message += alphabet[shifted_value]
    return encrypted_message
    

def decrypt(message, key):
    decrypted_message = ''
    pass  # TODO replace this line with your code.


print(encrypt('david',4))

