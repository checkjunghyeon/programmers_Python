def solution(arr):
    n = len(arr)
    count = [0, 0]
    quadtree(n, arr, 0, 0, count)
    return count

def quadtree(n, arr, row, col, count):
    first_value = arr[row][col]
    if all(arr[i][j] == first_value for i in range(row, row + n) for j in range(col, col + n)):
        count[first_value] += 1
        return

    half_n = n // 2
    quadtree(half_n, arr, row, col, count)              # upperLeft
    quadtree(half_n, arr, row, col + half_n, count)      # upperRight
    quadtree(half_n, arr, row + half_n, col, count)      # lowerLeft
    quadtree(half_n, arr, row + half_n, col + half_n, count)  # lowerRight
