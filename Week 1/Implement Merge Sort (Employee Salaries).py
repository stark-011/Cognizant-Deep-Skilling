def merge_sort(salaries):
    if len(salaries) <= 1:
        return salaries[:]

    mid = len(salaries) // 2
    left = merge_sort(salaries[:mid])
    right = merge_sort(salaries[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    salaries = [45000, 38000, 72000, 29000, 95000]
    sorted_salaries = merge_sort(salaries)
    print("Sorted salaries:", sorted_salaries)
