
arr = [1,2,3,4,5,6] 
def func(arr , left , right):
    if left>=right:
        return
    
    arr[left],arr[right] = arr[right],arr[left]
    
    func(arr , left+1 , right-1)

    
func(arr, 0, len(arr) - 1)
print(arr)

# time complexity0(N) and space complixity is o(N) ==> stack 