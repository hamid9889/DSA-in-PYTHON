s = "NITIN"
def func(s , left , right):
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return func(s , left +1 , right -1)
print(func(s, 0, len(s) - 1))

# time complexity o(N/2 => N) and space complwxity o(N ) ==> stack space