# Quick sort 
"""
1= Pick a Pivot
- it can be the first element  # we use this 
- it can br the last element 
- it can be the middle elemrnt
- it can be the randome element

2 = put pivot at its correct position / index

"""


nums = [3,1,2,6,7,8,4]

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            p_index = self.partition(arr, low, high)
            # Recursively sort elements before and after partition
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1
            while j >= low + 1 and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j
    
    """
    tc ans sc in best and avg case == TC = o(logN x N)
    SC == o(1)
    
    """
    """
    for wrost case -- TC = o(N x N -- N^2)
   space cimplexity of this sorting o(N )
    """
    
    