class Dp1:

    @staticmethod
    def value(i, j, matrix, letters):
        return int(matrix[letters.index(i)][letters.index(j)])

    @staticmethod
    def dp(str1, str2, letters, matrix, memo):
        if (str1, str2) in memo:
            return memo[(str1, str2)]

        if len(str1) == 0:
            return -4 * len(str2)  
        if len(str2) == 0:
            return -4 * len(str1)  

        match = Dp1.value(str1[0], str2[0], matrix, letters) + Dp1.dp(str1[1:], str2[1:], letters, matrix, memo)
        insert = -4 + Dp1.dp(str1, str2[1:], letters, matrix, memo) 
        delete = -4 + Dp1.dp(str1[1:], str2, letters, matrix, memo) 

        cost = max(match, insert, delete)
        memo[(str1, str2)] = cost
        return cost

    @staticmethod
    def align(str1, str2, letters, matrix):
        memo = {}
        Dp1.dp(str1, str2, letters, matrix, memo)
        
        aligned1, aligned2 = "", ""
        while str1 or str2:
            if memo[(str1, str2)] == Dp1.value(str1[0], str2[0], matrix, letters) + memo.get((str1[1:], str2[1:]), 0):
                aligned1 += str1[0]
                aligned2 += str2[0]
                str1, str2 = str1[1:], str2[1:]
            elif memo[(str1, str2)] == -4 + memo.get((str1, str2[1:]), 0):
                aligned1 += '*'
                aligned2 += str2[0]
                str2 = str2[1:]
            else:
                aligned1 += str1[0]
                aligned2 += '*'
                str1 = str1[1:]

        #aligned1 += str1 or '*' * len(str2)
        #aligned2 += str2 or '*' * len(str1)

        return aligned1, aligned2