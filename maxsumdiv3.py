class Temp:

    def maxSumDivThree(self, A):
        seen = [0, 0, 0]
        for a in A:
            for i in seen[:]:
                print(a, i)
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
                print(seen)
        return seen[0]

#lt = [2, 7, 6, 1, 4, 5]
#lt = [ 3, 1, 2]
lt = [7,2,4]

A = Temp()
print (A.maxSumDivThree(lt))
