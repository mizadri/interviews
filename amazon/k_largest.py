import heapq

def kLargest(arr, k):
    # Method 1: Using heapq.nlargest
    return heapq.nlargest(k, arr)

    # Alternative Method 2: Using heap directly
    # result = []
    # for num in arr:
    #     heapq.heappush(result, -num)  # Push negative values to simulate max heap
    # return [-heapq.heappop(result) for _ in range(k)]  # Pop and negate back

# Driver code
arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(kLargest(arr, k))  # Output: [50, 30, 23]