def binary_search(product_ids, target):
    left, right = 0, len(product_ids) - 1

    while left <= right:
        mid = (left + right) // 2

        if product_ids[mid] == target:
            return mid
        elif product_ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    product_ids = [101, 102, 103, 104, 105, 106]
    target = 104
    result = binary_search(product_ids, target)

    if result != -1:
        print(f"Product ID {target} found at index {result}")
    else:
        print(f"Product ID {target} not found")
