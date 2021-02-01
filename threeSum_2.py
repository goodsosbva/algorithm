numbers = [-4, -1, -1, 0, 1, 2]
numbers.sort()
threeZeros = []

for i in range(len(numbers) - 2):
    if i > 0 and numbers[i] == numbers[i - 1]:
        continue

    left, right = i + 1, len(numbers) - 1
    while left < right:
        sum = numbers[i] + numbers[left] + numbers[right]

        if sum > 0:
            right -= 1
        elif sum < 0:
            left += 1
        else:
            threeZeros.append([numbers[i], numbers[left], numbers[right]])
            while left < right and numbers[left] == numbers[left + 1]:
                left += 1
            while left < right and numbers[right] == numbers[right - 1]:
                right -= 1

            left += 1
            right -= 1

print(threeZeros)