
for num in range(0, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")

        if num % 2 == 0:
            print("even-fizzbuzz")
        else:
            print("odd-fizzbuzz")
    elif num % 3 == 0:
        print("fizz")

    elif num % 5 == 0:
        print("buzz")

    else:
        print(num)
