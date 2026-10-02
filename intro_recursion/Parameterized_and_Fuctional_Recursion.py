# Sum od 1 to n [parameterizes way]

def func(sum , i , n):
    if i > n:
        print(sum )
        return
    func(sum +i, i+1, n)
    
func(0, 1,10)   

# functional sum [1 to n]


'''
1 = create the flow
2 = create the base condition 

'''
def func(n):
    if n ==1:
        return 1
    
    return n + func(n-1)

print(func(4))

# time complexity o(N)  space complexity o(N) == This is actually stack space



