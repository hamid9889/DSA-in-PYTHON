
matrix = []
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)  
        c = len(matrix[0])

        rowtrac = [0 for _ in range (r)]
        coltrac = [0 for _ in range (c)]

        for i in range(0 , r):
            for j in range(0 , c):
                if matrix[i][j] == 0:
                    rowtrac[i] = -1
                    coltrac[j] = -1

        for i in range (0 , r):
            for j in range(0 , c):
                if rowtrac[i]== -1 or coltrac[j]== -1:
                    matrix[i][j] = 0




"""
time complexity is O ( 2 X (n X M)) ~~ O (N X M)


space complexity is O ( r + c)
"""





