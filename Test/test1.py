# numbers = [45, 73, 195, 53]
numbers = [3, 2, 4, 1]
computedNumbers = []
lenNumbers = len(numbers) - 1

for index, item in enumerate(numbers):
    # print(index, item)
    if index != lenNumbers:
        newNum = numbers[index] * numbers[index+1]
        computedNumbers.append(newNum)
    else:
        newNum = numbers[index] * numbers[0]
        computedNumbers.append(newNum)
    
print(computedNumbers)