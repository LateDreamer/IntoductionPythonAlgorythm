import random

def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]

def quick_select(seq, k , left=None, right=None):
    left = left or 0
    right = right or len(seq) - 1
    ipivot = random.randint(left, right)
    pivot = seq[ipivot]

    # 피벗을 정렬 범위 밖으로 이동한다.
    swap(seq, ipivot, right)
    swapIndex, i = left, left
    while i < right:
        if seq[i] < pivot:
            swap(seq, i, swapIndex)
            swapIndex += 1
        i += 1

    # 피벗 위치를 확정한다
    swap(seq, right, swapIndex)
    # 피벗 위치를 확인한다
    rank = len(seq) - swapIndex
    if k == rank:
        return seq[swapIndex]
    elif k < rank:
        return quick_select(seq, k, left=swapIndex+1, right=right)
    else:
        return quick_select(seq, k, left=left, right=swapIndex-1)

def find_k_largest_seq_quickselect(seq, k):
    # k번째로 큰 값을 찾는다
    kth_largest = quick_select(seq, k)

    # k번째보다 큰 값을 저장한다
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)
    return result

if __name__ == "__main__":
    seq = [3,10,4,5,1,8,9,11,5]
    k = 3
    print(find_k_largest_seq_quickselect(seq, k))