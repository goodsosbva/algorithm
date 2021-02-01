numbers = [1, 4, 3, 2, 5, 7]
sum = 0
pair = []
numbers.sort()

for i in numbers:
    pair.append(i)
    if len(pair) == 2:
        sum += min(pair)
        print(min(pair))
        pair = []

print("sum: ", sum)