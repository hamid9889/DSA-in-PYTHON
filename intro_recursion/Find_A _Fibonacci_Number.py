class Fibonacci:

    def func(self, n):
        if n <= 1:
            return n

        return self.func(n - 1) + self.func(n - 2)


obj = Fibonacci()

print(obj.func(6))
#time complexity is o( 2`N`) and space complexity o (2`N` )