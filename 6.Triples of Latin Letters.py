numbers_of_symbols = int(input())
for first_symbols in range(97, 97 + numbers_of_symbols):
    for second_symbols in range(97, 97 + numbers_of_symbols):
        for third_symbols in range(97, 97 + numbers_of_symbols):
            print(f'{chr(first_symbols)}{chr(second_symbols)}{chr(third_symbols)}')