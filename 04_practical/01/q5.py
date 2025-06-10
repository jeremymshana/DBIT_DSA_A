def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

string = "data structures and algorithms"
print(char_frequency(string))