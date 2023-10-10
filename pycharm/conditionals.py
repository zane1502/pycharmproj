
age = int(input("How old are you?"))

if 0 < age < 2:
    stage = 'baby'

elif age < 4:
    stage = 'toddler'

elif age < 13:
    stage = 'kid'

elif age < 20:
    stage = 'teen'

elif age <= 65:
    stage = 'adult'

elif age > 65:
    stage = 'elder'

else:
    print("Come again?")

print(f"That would mean that you are in your {stage} stage.")
