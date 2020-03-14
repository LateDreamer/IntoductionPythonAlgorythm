import heapq

def heap_sort1(seq):
    h = []
    for value in seq:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

def test_heap_sort1():
    seq = [3,5,2,6,8,1,0,3,5,6,2]
    assert(heap_sort1(seq) == sorted(seq))
    print("테스트 통과")

if __name__ == "__main__":
    test_heap_sort1()