text = input('Enter any text: ')
upper_letters_count = 0
lower_letters_count = 0
digits_count = 0
symbols_count = 0
for letters in text:
    full_letters_count = len(letters)
    if letters.islower():
        lower_letters_count += 1
    elif letters.isupper():
        upper_letters_count += 1
    elif letters.isdigit():
        digits_count += 1
    else:
        symbols_count += 1
result = upper_letters_count + lower_letters_count + digits_count + symbols_count
a = (upper_letters_count / result) * 100
b = (lower_letters_count / result) * 100
c = (digits_count / result) * 100
d = (symbols_count / result) * 100
print(round(a), '%', 'Upper')
print(round(b), '%', 'Lower')
print(round(c), '%', 'Digit')
print(round(d), '%', 'Symbol')
