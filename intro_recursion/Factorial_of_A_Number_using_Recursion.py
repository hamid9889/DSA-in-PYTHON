def factorial(num ):
    if num==1 or num ==0:
       
        return 1
    else:
        return (num * factorial(num-1))
    
print(factorial(5))    

#time complexity is o(n) and Space complaxity o(N) => stack space