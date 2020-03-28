I decided to use a Python dictionary to build a Huffman Tree because it allows
for O(1) insertion and extraction of data. Also, the key and value items can
readily be flipped for decoding purposes. The complexity of the encoding
function has time complexity of 3n + n log n, while the decoding functions has
time complexity of 2n. The space complexity is O(n).
