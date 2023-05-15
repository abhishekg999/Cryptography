import base64

def hex_to_base64(hex):
    byte_array = bytearray.fromhex(hex)
    return base64.b64encode(byte_array).decode()
    
def hamming_distance(str1, str2):
    assert len(str1) == len(str2)

    str1_bits = ''.join(format(ord(i), '08b') for i in str1)
    str2_bits = ''.join(format(ord(i), '08b') for i in str2)

    total = 0
    for a, b in zip(str1_bits, str2_bits):
        total += a != b
    
    return total

if __name__ == "__main__":
    HEX_STR = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    assert hex_to_base64(HEX_STR) == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    print(hamming_distance('this is a test', 'wokka wokka!!!'))