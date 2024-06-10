def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 왼쪽 자식이 루트보다 크면 왼쪽 자식을 가장 큰 값으로 설정
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재 가장 큰 값보다 크면 오른쪽 자식을 가장 큰 값으로 설정
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 가장 큰 값이 루트가 아니면 교환하고 재귀적으로 힙을 구성
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 배열을 힙으로 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 요소를 힙에서 추출하여 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 현재 루트(최대값)를 배열의 끝으로 이동
        heapify(arr, i, 0)  # 배열의 나머지에 대해 힙을 다시 구성


# 테스트 배열
arr = [1, 2, 6, 8, 4, 5, 3, 7, 9]
heap_sort(arr)
print("Sorted array:", arr)
