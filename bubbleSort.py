numbers = [65,35,74,23,97]

n = len(numbers)
for i in range(n-1):
    for j in range(n-1-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            
print(numbers)
