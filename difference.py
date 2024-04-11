# initialise sum_of_squares = 0
sum_of_squares = 0
# initialise sum = 0
sum = 0
# initialise i = 1
# i = 1

# while i <= 100
# while i <= 100:
for i in range(1, 101):
    # sum_of_squares = sum_of_squares + i * i
    # sum_of_squares = sum_of_squares + i * i
    sum_of_squares += i * i
    # sum = sum + i
    # sum = sum + i
    sum += i
    # i = i + 1
    # i = i + 1


# square_of_sum = sum * sum
square_of_sum = sum * sum

# diff = square_of_sum - sum_of_squares
diff = square_of_sum - sum_of_squares

# display diff
print(diff)