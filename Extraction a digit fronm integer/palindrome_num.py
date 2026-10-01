n = 1221
num = n 
result = 0 
while num  >0:
    ld = num%10
    result = (result*10)+ ld
    num = num//10
if result == n :
    print(" number palindrome")
else :
    print(" num is not palindrome")   

# time complexity of this is O(log n) and space complexity is O(1)
    
     