def func(num ):
    if num==1:
       
        return 1
    return (num * func(num-1))
    
print(func(5))    