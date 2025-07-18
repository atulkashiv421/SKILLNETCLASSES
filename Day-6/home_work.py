input_string = "aaabbbcccdddee"

input_string = input_string.upper()


char_count = {}


for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"{char}= {count}")
