import heapq

# Creating an initial heap
h = [10, 20, 15, 30, 40]
heapq.heapify(h)

# Appending an element
heapq.heappush(h, 5)
print(h)
# Pop the smallest element from the heap
min = heapq.heappop(h)

print(h)

print("Smallest:", min)
print(h)