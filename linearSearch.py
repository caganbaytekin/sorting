def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    target = 22

    result = linear_search(numbers, target)

    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")
