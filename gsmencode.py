import sys

import gsm0338


def __create_septets__(octets: bytes) -> (bytes, int):
    num_bits = 0
    data = 0
    septets = bytearray()
    for i in range(len(octets)):
        gsm_char = octets[i]
        data |= (gsm_char << num_bits)
        num_bits += 7
        while num_bits >= 8:
            septets.append(data & 0xff)
            data >>= 8
            num_bits -= 8
    if num_bits > 0:
        septets.append(data & 0xff)
    return bytes(septets), len(octets) % 8


if __name__ == '__main__':
    octets = sys.argv[1].encode('gsm03.38')
    septets, sparse = __create_septets__(octets)
    print("sparse bits: %d" % sparse)
    print("encoded (hex): %s" % septets.hex())
