
counter = 1

while counter <= 100:

    if counter % 5 == 0 and counter % 3 == 0:
        print("fizzbuzz")

    elif counter % 3 == 0:
        print("fizz")

    elif counter % 5 == 0:
        print("buzz")

    else:
        print(counter)
    counter += 1





