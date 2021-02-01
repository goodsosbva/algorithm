numbers = [1, 4, 3, 2, 6, 5]
numbers.sort()
pair = []
sum = 0
sum1 = 0
test = {}

for i in numbers:
    # sum += numbers[0]
    if i % 2 == 1:
        sum += i

for i, n in enumerate(numbers):
    test[i] = n
    # sum += numbers[0]
    if i % 2 == 0:
        sum1 += n

print(test)
print(sum)
print(sum1)