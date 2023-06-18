# please provide a two-digit integer number

two_digit_number = int(input("Provide two digit number: "))

tens_digit = two_digit_number // 10

ones_digit = two_digit_number % 10

print(f"Number for ten's digit is: {tens_digit} and Number for one's digit is: {ones_digit}")

