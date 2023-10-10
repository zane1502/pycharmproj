prime_numbers = []

for i in range(1, 1001):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % (i ** 0.5) != 0:
        prime_numbers.append(i)

    elif i == 2 or i == 3 or i == 5 or i == 7:
        prime_numbers.append(i)

print(prime_numbers)


# this code works well enough if you are trying to work with integers between 1 and 100, but the larger the number
# becomes, the harder it is to continue with this logic. for example, if we use a range of 1-1000000, numbers like 169
# and 289 would pass the conditions when they are not actually prime numbers. we would have to try to figure out all the
# base cases for the prime numbers which is not realistic. so we have to figure out a better logic that will allow us to
# solve for every scenario.




