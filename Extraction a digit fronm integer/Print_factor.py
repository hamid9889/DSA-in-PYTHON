# normal solution 

num = 12
result = []
for i in range(1 , num+1):
    if num%i ==0:
        result.append(i)
        
print(result)
# teime complexity of this is O(n) and space complexity is O(K) where k is the number of factors of n


# optimal solution 

n = 15
num = n 
result = []
for i in range(1 , num//2):
    if num % i ==0:
        result.append(i)
        
result.append(num)
print(result)   

# time complexity of this is O(n/2) and space complexity is O(K) where k is the number of factors of n

# besr optimal solution 

from math import sqrt
n = 16
num = n
result = []
for i in range(1 ,int(sqrt(n))+1):
    if num%i ==0:
        result.append(i)
        if num//i != i:
            result.append(num//i)
 
result.sort()           
print(result)            

#time complexity of this is O(sqrt(n)= o(Nlog(N)))) and space complexity is O(K) where k is the number of factors of n
 

