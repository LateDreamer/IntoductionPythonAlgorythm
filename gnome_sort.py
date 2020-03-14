def gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
        print(seq)
    return seq

def test_gnome_sort():
    seq = [5,3,2,4]
    assert(gnome_sort(seq) == sorted(seq))
    print("테스트 통과")

if __name__ == "__main__":
    test_gnome_sort() 