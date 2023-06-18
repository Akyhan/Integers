# please provide a three-digit integer number

three_digit_number_1 = int(input("Provide three digit number: "))

three_digit_number_2 = int(input("Provide three digit number: "))


#The variable provides ten's digit
tens_digit_1 = (three_digit_number_1 % 100) // 10
tens_digit_2 = (three_digit_number_2 % 100) // 10

#The variable provides last digit
one_digit_1 = (three_digit_number_1 % 10)
one_digit_2 = (three_digit_number_2 % 10)

#The variable provides hundred's digit
hundreds_digit_1 = three_digit_number_1 // 100
hundreds_digit_2 = three_digit_number_2 // 100

sum_hundreds = hundreds_digit_1 + hundreds_digit_2
product_hundreds = hundreds_digit_1 - hundreds_digit_2

sum_tens = tens_digit_1 + tens_digit_2
product_tens = tens_digit_1 - tens_digit_2

sum_ones = one_digit_1 + one_digit_2
product_ones = one_digit_1 - one_digit_2


print(f"Number for sum of hundreds's digit is: {sum_hundreds} ")

print(f"Number for sum of ten's  digit is: {sum_tens} ")

print(f"Number for sum of one's  digit is: {sum_ones} ")

print(f"Number for product of hundred's  digit is: {product_hundreds} ")

print(f"Number for product of ten's  digit is: {product_tens} ")

print(f"Number for product of ones's  digit is: {product_ones} ")







