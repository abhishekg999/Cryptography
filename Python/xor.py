from pprint import pprint


def fixed_xor(buf1, buf2):
    assert len(buf1) == len(buf2)

    buf1_bytes = bytearray.fromhex(buf1)
    buf2_bytes = bytearray.fromhex(buf2)
    xor_bytes = bytes(a ^ b for (a, b) in zip(buf1_bytes, buf2_bytes))

    return xor_bytes.hex()


def single_byte_xor(buf: bytes, key: bytes):
    assert len(key) == 1

    key_buf = key * len(buf)

    return fixed_xor(buf.hex(), key_buf.hex())


if __name__ == "__main__":
    A = "1c0111001f010100061a024b53535009181c"
    B = "686974207468652062756c6c277320657965"

    assert fixed_xor(A, B) == "746865206b696420646f6e277420706c6179"

    SINGLE_BYTE_XORED = (
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    )
    code_bytes = bytearray.fromhex(SINGLE_BYTE_XORED)

    possibilities = []
    for i in range(256):
        key = bytes([i])
        possibilities.append(
            bytearray.fromhex(single_byte_xor(code_bytes, key)).decode(errors="replace")
        )

    from english import score_english_string

    possibilities.sort(key=score_english_string)

    with open("challenge-text/4.txt", "r") as f:
        data = f.read().split()

    
    # find the most likely string from each line in data
    best_of_each_line = []
    for line in data:
        line_bytes = bytearray.fromhex(line)
        line_possibilities = []

        for i in range(256):
            key = bytes([i])
            line_possibilities.append(
                bytearray.fromhex(single_byte_xor(line_bytes, key)).decode(errors='replace')
            )
        
        line_possibilities.sort(key=score_english_string)


        best_of_each_line.append(line_possibilities[0])
    
    best_of_each_line.sort(key=score_english_string)
    pprint(best_of_each_line[:5])

