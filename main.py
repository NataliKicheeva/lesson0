# "1st program"
print(9 ** 0.5 * 5)

# "2st program"
print(9.99 > 9.98 and 1000 != 1000.1)

# "3rd program"
print((1234 % 2000 // 10) + (5678 % 1000 // 10))

# "4ht program)
num1 = 13.42
num2 = 42.13
int_part1 = int(num1)
int_part2 = int(num2)
frac_part1 = int((num1 - int_part1) * 100)
frac_part2 = int((num2 - int_part2) * 100)
result = (int_part1 == frac_part2) or (int_part2 == frac_part1)
print(result)
