def bubble_sort(arr):
    n = len(arr)
    print(f"original list: {arr}\n")

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        print(f"pass {i + 1}: {arr}")

        # Both of these lines must be indented by exactly 8 spaces
        # so Python knows they belong to the outer 'for i in range(n):' loop!
        if not swapped:
            break

if __name__ == "__main__":
    example_list = [64, 25, 12, 22, 11]
    bubble_sort(example_list)
    print(f"\nFinal sorted list: {example_list}")
