def sum_of_squares(numbers):
    # initialize the sum to zero
    total = 0
    # loop through each number in the list
    for num in numbers:
        # square the number and add it to the sum
        total += num ** 2
    # return the sum
    return total
