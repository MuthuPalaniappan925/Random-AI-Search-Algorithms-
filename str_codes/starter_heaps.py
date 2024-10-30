##Import something which may be helpful !!
'''In a Min-Heap, the value of each node is less than or equal to the values of its children.
In a Max-Heap, the value of each node is greater than or equal to the values of its children.'''
import heapq

min_heap1 = []

heapq.heappush(min_heap1, 10)
heapq.heappush(min_heap1, 9)
heapq.heappush(min_heap1, 50)
heapq.heappush(min_heap1, 15)
heapq.heappush(min_heap1, 30)

#print("Min-Heap after adding elements:", min_heap1)

smallest = heapq.heappop(min_heap1)
print("Smallest element removed:", smallest)
print("Min-Heap after removal:", min_heap1)

heapq.heappush(min_heap1, 1)
heapq.heappush(min_heap1, 8)
#print("Min-Heap after adding elements:", min_heap1)

##How to convrt a list into a heap
data = [13, 5, 7, 2]
heapq.heapify(data)
#print("Heapified list -> ", data)

##Then how to do max heap ? -> Multiply the elements by -1 and then do the heapify (negate the elements to get the original values)