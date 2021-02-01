numbers = [-4, -1, -1, 0, 1, 2]
numbers.sort()
threeSum = []

for i in range(len(numbers) - 2):
    if i > 0 and numbers[i] == numbers[i - 1]:
        print("i range")
        print("number[%i]:" %i, numbers[i])
        continue
    for j in range(i + 1, len(numbers) - 1):
        if j > i + 1 and numbers[j] == numbers[j - 1]:
            print("j range")
            print("number[%i]:" %i, numbers[j])
            print("number[%i]:" %(i - 1), numbers[j - 1])
            continue
        for k in range(j + 1, len(numbers)):
            if k > j + 1 and numbers[k] == numbers[k - 1]:
                print("number[k]:", numbers[k])
                continue
            if numbers[i] + numbers[j] + numbers[k] == 0:
                threeSum.append((numbers[i], numbers[j], numbers[k]))


print(threeSum)