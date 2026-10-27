def bubble_sort(students, order="ascending"):
    """Return a sorted copy using Bubble Sort."""
    result = [student.copy() for student in students]
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            left = result[j]["marks"]
            right = result[j + 1]["marks"]
            should_swap = left > right if order == "ascending" else left < right
            if should_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(students, order="ascending"):
    """Return a sorted copy using Selection Sort."""
    result = [student.copy() for student in students]
    n = len(result)
    for i in range(n):
        target = i
        for j in range(i + 1, n):
            current = result[j]["marks"]
            best = result[target]["marks"]
            better = current < best if order == "ascending" else current > best
            if better:
                target = j
        result[i], result[target] = result[target], result[i]
    return result
