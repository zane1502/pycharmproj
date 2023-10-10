# 6-1.


# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

Dad = {'first_name': 'Pius', 'last_name': 'Achilike', 'age': 52, 'city': 'Owerri'}

print(f"{Dad}\n")

# 6-2.

# Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favourite_numbers = {'Sam': 7,
                     'fidelis': 23,
                     'ebuka': 34,
                     'Success': 33
                     }

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

new_words = {'iteration': 'the process of automatically repeating a block of code',
             'concatenate': 'to combine two or more strings',
             'loop': 'a control structure that repeats a block of code',
             'pseudocode': 'the english interpretation of code'}

for k, v in new_words.items():  # k and v are the variables that contain every key and value in the loop, respectively
    print(f"{k.title()}: {v}\n")

# 6-4.
#
# Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

new_words['object'] = 'an instance of a class'
new_words['method'] = 'a function which is defined under a class and associated with an object'

for k, v in new_words.items():
    print(f"\t{k.upper()}: {v}\n")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.

rivers_in_africa = {'Niger': 'Nigeria', 'Benue': 'Nigeria', 'Senegal': 'Senegal'}

for river, country in rivers_in_africa.items():
    print(f"The river {river.title()} is a very popular river in {country.title()}")

# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

poll_takers = ['Sam', 'emma', 'patrick', 'fidelis']

for taker in poll_takers:
    if taker in favourite_numbers.keys():
        print(f"Hey {taker.title()}, thanks for taking the poll!\n")

    elif taker not in favourite_numbers.keys():
        print(f"{taker.title()}, please take the poll asap!\n")


# 6-7.
#
# People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
#

Mum = {'first_name': 'Tobechi', 'last_name': 'Eze', 'age': 46, 'city': 'Owerri'}

Me = {'first_name': 'Samuel', 'last_name': 'Achilike', 'age': 20, 'city': 'Owerri'}

people = [Dad, Me, Mum]

for person in people:

    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and hails from {person['city']}")


# I didn't do exercise 6-8 and 6-9 because they were more or less like 6-7

# 6-10.
#
# Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favourite_numbers['Sam'] = [7]
favourite_numbers['Success'] = [3, 5, 33]
favourite_numbers['fidelis'] = [3, 55, 2]
favourite_numbers['ebuka'] = [6, 5, 3]

for name, fav in favourite_numbers.items():
    if len(fav) > 2:
        print(f"{name.title()}'s favourite numbers are {str(fav)}\n")

    else:
        print(f"{name.title()}'s favourite number is {str(fav)}\n")

# 6-11.

# Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'abuja': {'country': 'Nigeria', 'population': 8000000, 'fact': 'Abuja was formed out of six states in the north'
                                                                   'central'},
    'kano': {'country': 'Nigeria', 'population': 20000000, 'fact': 'Kano is one of the oldest cities in africa'},
    'lagos': {'country': 'Nigeria', 'population': 25000000, 'fact': 'Lagos has the largest population of '
                                                                    'english speakers'}
}

for city_name, city_info in cities.items():
    print(f"This is {city_name.title()}, located in {city_info['country']}"
          f" with a population of over {city_info['population']}. {city_info['fact']}\n")

# 6-12.

# Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs from this chapter,
# and extend it by adding new keys and values,
# changing the context of the program or improving the formatting of the output

message = input("What's your name?")

print(f"Hello {message.title()}")

# i, j = {'hello', 2}
#
# print(f"{i}, you requested for {j}")
