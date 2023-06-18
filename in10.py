# please provide a three-digit integer number

three_digit_number = int(input("Provide three digit number: "))

tens_digit = (three_digit_number % 100) // 10


print(f"Number for hundreds's digit is: {tens_digit}")



