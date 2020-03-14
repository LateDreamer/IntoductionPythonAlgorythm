def insertion_sort(seq):
    for i in range(1,len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        print(seq)
    return seq

def insertion_sort_rec(seq, i=None):
    if i is None:
        i = len(seq) -1
    if i == 0:
        return i
    insertion_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

def test_insertion_sort():
    seq = [11,3,28,43,9,4]
    assert(insertion_sort(seq) == sorted(seq))
    assert(insertion_sort_rec(seq) == sorted(seq))
    print("테스트 통과")

if __name__ == "__main__":
    test_insertion_sort()