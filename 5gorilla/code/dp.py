class Dp:
    
    # def dp(str1, str2, letters, matrix): 
    #     if str1 == str2:
    #         return (str1, str2, )
    #     else:
    #         dprec(str1, str2, letters, matrix)
    @staticmethod
    def value(i,j, matrix, letters):
        print(matrix[letters.index(i)][letters.index(j)])
        return matrix[letters.index(i)][letters.index(j)]
    
    @staticmethod
    def dprec(str1, str2, letters, matrix):
        if str1 == 0 and str2 == 0:
            return 0
        elif str1 == 0:
            return -4 * len(str2)
        elif str2 == 0:
            return -4 * len(str1)
        else:
            return max(Dp.value(str1[0], str2[0], matrix, letters) + dprec(str1[1:], str2[1:], letters, matrix), 
                -4 + Dp.dprec(str1, str2[1:], letters, matrix)
                -4 + Dp.dprec(str1[1:], str2, letters, matrix))





