# please provide a two-digit integer number

first_digit = int(input("Provide two digit number: "))

second_digit = int(input("Provide two digit number: "))

tens_digit_1 = first_digit // 10

tens_digit_2 = second_digit // 10

ones_digit_1 = first_digit % 10

ones_digit_2 = second_digit % 10

sum_tens_digit = tens_digit_1 + tens_digit_2

product_tens_digit = tens_digit_1 - tens_digit_2

sum_ones_digit = ones_digit_1 + ones_digit_2

product_ones_digit = ones_digit_1 - ones_digit_2

print(f"Sum of ten's digit is: {sum_tens_digit}")

print(f"Sum of ones's digit is: {sum_ones_digit}")

print(f"Product of ten's digit is: {product_tens_digit}")

print(f"Product of one's digit is: {product_ones_digit}")




