#Selection Sort

# Time Complexity : O(N*N)

from typing import List

def selectionSort(arr: List[int]) -> None:
        n = len(arr)
        for i in range(n):
            fIndex = i
            for j in range(i+1, n):
                if arr[j] < arr[fIndex]:
                    fIndex = j
        arr[fIndex], arr[i] = arr[i], arr[fIndex]