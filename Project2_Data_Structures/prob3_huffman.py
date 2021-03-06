# @Author: otrejo
# @Date:   2020-03-05T00:12:05-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-27T20:48:36-04:00



import sys

def huffman_encoding(data):
    # Make frequency dictionary
    d = {}
    for char in data:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    # Make ordered list of tuples
    l_tuples = sorted(d.items(), key=lambda tup: tup[1], reverse=True)

    # Make tree
    t = {}
    base = '1'
    for tup in l_tuples:
        t[tup[0]] = base
        base = '0' + base

    # Encode data
    encoded_data = ''
    for char in data:
        encoded_data += t[char]

    return encoded_data, t

def huffman_decoding(data,tree):
    # Flip tree dictionary
    d = {}
    for key in tree:
        d[tree[key]] = key
    print(d)
    # Decode data
    base = ''
    decoded_data = ''
    for char in data:
        if char == '1':
            decoded_data += d[base + char]
            base = ''
        else:
            base += char

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    # Test 1
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # "The bird is the word"

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # Test 2
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # 40
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # "00000010100110000000100010000100000110001000000001100000000010100110000000000100000000000100001000001"

    decoded_data = huffman_decoding(encoded_data, tree)
    # Test 3
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # "The bird is the word"
