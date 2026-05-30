key = int(input())
number_of_lines = int(input())
messages = ""

for i in range(number_of_lines):
    letter = input()
    new_letter = ord(letter)
    total_new_letter = key + new_letter
    char_to_add = chr(total_new_letter)
    messages += char_to_add

print(messages)