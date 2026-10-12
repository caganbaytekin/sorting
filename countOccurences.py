def count_occurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 2, 5, 2]
    target = 2

    print("Occurrences:", count_occurrences(numbers, target))
