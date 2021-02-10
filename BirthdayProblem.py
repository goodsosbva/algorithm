import random

Try = 100000
sameBirthday = 0

for _ in range(Try):
    birthdays = []


    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            sameBirthday += 1
            break

        birthdays.append(birthday)
        #print(birthdays, end=" ")

print(f'{sameBirthday / Try * 100}%')