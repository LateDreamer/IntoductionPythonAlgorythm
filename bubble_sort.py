def bubble_sort(seq):
    length = len(seq) -1
    for num in range(length, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                print(seq)

    return seq

def test_bubble_sort():
    seq = [4,5,2,1,6,2,7,10,13,8]
    assert(bubble_sort(seq) == sorted(seq))
    print("테스트 동과!")

if __name__ == "__main__":
    test_bubble_sort()