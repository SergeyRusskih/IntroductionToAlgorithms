# O(log n), maintains the max-heap property
# assumes that the binary trees rooted at LEFT(i) and RIGHT(i) are maxheaps, 
# but that A[i] might be smaller than its children, thus violating the max-heap
# property. HEAPIFY lets the value at A[i] “float down” in the max-heap so
#that the subtree rooted at index i obeys the max-heap property.
def heapify(i, arr):
    left_index = left(i, arr)
    right_index = right(i, arr)

    if left_index <= len(arr) and arr[left_index] > arr[i]:
        swap(i, left_index, arr)
        return heapify(left_index, arr)
    elif right_index <= len(arr) and arr[right_index] > arr[i]:
        swap(i, right_index, arr)
        return heapify(right_index, arr)
    else:
        return arr

def swap(x, y, arr):
    arr[x] += arr[y]
    arr[y] = arr[x] - arr[y]
    arr[x] -= arr[y]

    # O(n), produces a maxheap from an unordered input array
def build_heap(arr):
    pass

    # O(n lg n), sorts an array in place
def heapsort(arr):
    pass

# O(lg n), allow the heap data structure to implement a priority queue
# MAX-HEAP-INSERT
def insert():
    pass

# HEAP-EXTRACT-MAX
def extract():
    pass

# HEAP-INCREASE-KEY
def increase_key():
    pass

# HEAP-MAXIMUM
def heap_maximum():
    pass

def parent(i, arr):
    return i // 2

def left(i, arr):
    return 2 * i

def right(i, arr):
    return (2 * i) + 1



def test_heapify():
    arr = [2, 16, 14, 12, 8, 7, 9, 3, 4, 1]
    res = heapify(0, arr)
    assert res == [16, 14, 8, 12, 4, 7, 9, 3, 2, 1]