# # # 7-1.
# # #
# # # Rental Car: Write a program that asks the user what kind of rental car they
# # # would like. Print a message about that car, such as “Let me see if I can find you
# # # a Subaru.”
# #
# # cars = ['subaru', 'toyota', 'lexus']
# #
# # user_request = input("What rental car would you like? \n")
# #
# # if user_request in cars:
# #     print(f"We have actually do have a {user_request}!")
# #
# # elif user_request not in cars:
# #     print(f"We don't have a {user_request.title()}"
# #           f"\nHere's a list of vehicles we have in stock though: \n")
# #     for i in cars:
# #         print(f"{i}\n")
# #
# # # 7-2. Restaurant Seating: Write a program that asks the user how many people
# # # are in their dinner group. If the answer is more than eight,
# # print a message saying they’ll have to wait for a table.
# # # Otherwise, report that their table is ready.
# #
# # table_reserve = int(input("How many seats would you like reserved?"))
# #
# # if table_reserve > 8:
# #     print("Sorry, you would need to wait for a seat")
# #
# # elif table_reserve <= 8:
# #     print("Your table is ready")
# #
# # # 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# # # number is a multiple of 10 or not.
# #
# number = int(input("Pick a number!"))
#
# if number % 5 == 0 and  number % 2 == 0:
#     print(f"{number} is divisible by 10")
#
# else:
#     print(f"{number} is not divisible by 10")
#

prompt = f"Tell me something to repeat to you \n"
prompt += "Type 'quit' to quit"

# msg = ""
# while msg != 'quit':
#     msg = input(prompt)
#
#     if msg != 'quit':
#         print(msg)

active = True

msg = input(prompt)


multiples_of_ten = []

# current_num = 10
#
# while current_num <= 100:
#     multiples_of_ten.append(current_num)
#     current_num += 10
#
# print(multiples_of_ten)

# for i in range(1, 101):
#     if i % 10 == 0:
#         multiples_of_ten.append(i)
#
# print(multiples_of_ten)

