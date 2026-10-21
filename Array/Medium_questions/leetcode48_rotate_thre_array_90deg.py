matrix = [----------]

n = len(matrix)
for i in range(0 , n-1):
    for j in range(i+1 , n):
        
        matrix[i][j], matrix[j][i] = matrix[i][j],matrix[j][i]
        
for i in range(0, n):
    matrix[i].reverse()
    
    
    """
    time complexirty is the o(N)
    space complexity o(1)
        """
            