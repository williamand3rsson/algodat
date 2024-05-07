class Dp:

    @staticmethod
    def value(i, j, matrix, letters):
        return int(matrix[letters.index(i)][letters.index(j)])

    @staticmethod
    def valueAll(tp, matrix, letters):
        sum = 0
        for i in range(len(tp[0])): 
            key = tp[0][i]  
            value = tp[1][i] 
            if key == '*' or value == '*':
                sum = sum - 4
            else:
                sum = sum + Dp.value(key, value, matrix, letters)
        return sum


    @staticmethod
    def newMax(tp1, tp2, tp3, matrix, letters):
        value1 = Dp.valueAll(tp1, matrix, letters)
        value2 = Dp.valueAll(tp2, matrix, letters)
        value3 = Dp.valueAll(tp3, matrix, letters)
        best = max(value1, value2, value3)
        if best == value1:
            return tp1
        elif best == value2:
            return tp2
        else:
            return tp3

    @staticmethod
    def dprec(str1, str2, letters, matrix, memo):
        if (str1, str2) in memo: 
            return memo[(str1, str2)]
        if len(str1) == 0 and len(str2) == 0:
            return ("","")
        elif len(str1) == 0:
            return ('*' * len(str2), str2)
        elif len(str2) == 0:
            return (str1, '*' * len(str1))
        else:
            keep = Dp.dprec(str1[1:], str2[1:], letters, matrix, memo)
            switchL = Dp.dprec(str1, str2[1:], letters, matrix, memo)
            switchR = Dp.dprec(str1[1:], str2, letters, matrix, memo)
            result = Dp.newMax(
                        (str1[0] + keep[0], str2[0] + keep[1]),
                        ('*' + switchL[0], str2[0] + switchL[1]), 
                        (str1[0] + switchR[0], '*' + switchR[1]),
                        matrix, 
                        letters
                        )
            memo[(str1, str2)] = result 
            return result

# def dp(str1, str2, letters, matrix): 
    #     if str1 == str2:
    #         return (str1, str2, )
    #     else:
    #         dprec(str1, str2, letters, matrix)
    
    # @staticmethod
    # def value(i, j, matrix, letters):
    #     return int(matrix[letters.index(i)][letters.index(j)])

    # @staticmethod
    # def valueT(value, i, j):
    #     return value

    # @staticmethod
    # def dprec(str1, str2, letters, matrix):
    #     if len(str1) == 0 and len(str2) == 0:
    #         return 0
    #     elif len(str1) == 0:
    #         return -4 * len(str2)
    #     elif len(str2) == 0:
    #         return -4 * len(str1)
    #     else:
    #         print(str1, str2)
    #         return max(Dp.valueT(Dp.value(str1[0], str2[0], matrix, letters) + Dp.dprec(str1[1:], str2[1:], letters, matrix), str1, str2), 
    #                 Dp.valueT(-4 + Dp.dprec(str1, str2[1:], letters, matrix), str1, str2),
    #                 Dp.valueT(-4 + Dp.dprec(str1[1:], str2, letters, matrix), str1, str2))


