# provide three digit number

three_digit_number = int(input("provide three digit number: "))

swap_number = (three_digit_number // 100 * 10) + ((three_digit_number% 100) // 10) + (three_digit_number % 10 * 100)

print("Result of swap is: ", swap_number)