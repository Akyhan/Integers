# please provide a two-digit integer number

two_digit_number = int(input("Provide two digit number: "))

swapped_digits = (two_digit_number % 10) * 10 + (two_digit_number // 10)

print(f"Number of initial digit: {two_digit_number}")

print(f"Number of swapped digit: {swapped_digits}")



