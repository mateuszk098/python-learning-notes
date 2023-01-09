"""
Simple example of XOR encoding.
"""


def xor_encode_decode(text, encode_key):
    result = [chr(ord(letter) ^ ord(encode_key)) for letter in text]
    return "".join(result)


s1 = "Hello there!"

s1_encoded = xor_encode_decode(s1, "#")
print(s1_encoded)

s1_decoded = xor_encode_decode(s1_encoded, "#")
print(s1_decoded)
