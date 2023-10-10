usernames = ['admin', 'sam', 'ife', 'ebube', 'rice']

for i in usernames:
    if i == 'admin':
        print("Hello Admin, would you like to see the status report?")
    else:
        print(f"Hello {i}")

for i in usernames:
    usernames.clear()

print(usernames)

if len(usernames) == 0:
    print("We need more users")
