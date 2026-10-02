
#Recursion using parameter

def func(x , n ):
    if n == 0:
        return
    
    print(x)
    func(x, n-1)

func(15 , 4)    

# print 1 to N using Recursion 
# Head Recursion
def func(i , n):
    if i > n:
        return
    
    print(i)
    func(i+1, n)

func(1, 4) 

# Tail Recursion Backtracking , N to 1 using Recursion
   
def func(i , n):
    if i > n:
        return
    
    func(i+1, n)
    print(i)

func(1, 4)    


# N to 1 using Head

def func(n):
    if n ==0:
        return
    print(n)
    func(n-1)
    
func(4)    
# 1 ti N using a tail

def func(n):
    if n ==0:
        return
    
    func(n -1)
    print(n)

func( 4)

















