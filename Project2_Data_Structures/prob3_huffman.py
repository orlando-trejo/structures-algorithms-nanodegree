import sys

def huffman_encoding(data):
    dict = {}
    for char in data:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    l_tuples = sorted(dict.items(), key=lambda tup: tup[1], reverse=True)
    for tup in l_tuples:
        print(tup)

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}


a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

huffman_encoding(a_great_sentence)
