n = 153
num = n 
total = 0
nod = len(str(n))

while num >0:
    ld = num %10
    
    total = total +(ld ** nod)
    num =num//10
    
print(total == n) 

# time complexity of this is O(log n) and space complexity is O(1)