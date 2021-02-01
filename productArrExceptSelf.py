p = 1
nums = [1, 2, 3, 4]
output = []

for i in range(0, len(nums)):
    output.append(p)
    p = p * nums[i]
    print("i: ", i)
    print(p)

print("output:", output)

p = 1

for i in range(len(nums) - 1, 0 - 1, -1):
    print("p:", p)
    output[i] = output[i] * p
    print("output: ", output[i])
    p = p * nums[i]
    

print(output)