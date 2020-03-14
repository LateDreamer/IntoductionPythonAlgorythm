from heap import Heap # 7.4챕터에 heap.py 만든 적 없음 ???

def heap_sort2(seq):
    s = list(seq)
    heap = Heap(s)
    res = []
    for _ in range(len(s)):
        res.insert(0, heap.extract_max())
    return res

def test_heap_sort2():
    seq = [3,5,2,6,8,1,0,3,5,6,2]
    assert(heap_sort2(seq) == sorted(seq))
    print("테스트 통과")

if __name__ == "__main__":
    test_heap_sort2()