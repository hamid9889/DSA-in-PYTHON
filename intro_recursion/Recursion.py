# # when a func call it self called Recursion 
# def greed():
#     print(" hamid")
    
    
# greed()    

count = 0
def func():
    if count == 4:
        return
    count +=1
    func()

print("hamid")    
#time complexity of this is O(n+1)==o(n) and space complexity is O(n+1)==0(n) where n is the number of recursive calls





