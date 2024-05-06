class Dp:
    
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


    @staticmethod
    def value(i, j, matrix, letters):
        return int(matrix[letters.index(i)][letters.index(j)])

    @staticmethod
    def valueAll(tp):
        sum = 0
        for key, value in tp:
            if key == '*' or value == '*':
                sum = sum - 4
            else:
                sum = sum + Dp.value(key, value, matrix, letters)
        return sum

    @staticmethod
    def newMax(new1, tp1, new2, tp2, new3, tp3):
        tp1 = (new1[0] + tp1[0], new1[1] + tp1[1])
        tp2 = (new2[0] + tp2[0], new2[1] + tp2[1])
        tp3 = (new3[0] + tp3[0], new3[1] + tp3[1])
        print(tp1)
        return max(Dp.valueAll(tp1), Dp.valueAll(tp2), Dp.valueAll(tp3))

    @staticmethod
    def dprec(str1, str2, letters, matrix):
        if len(str1) == 0 and len(str2) == 0:
            return ("","")
        elif len(str1) == 0:
            return ("*" * len(str2), str2)
        elif len(str2) == 0:
            return (str1, "*" * len(str1))
        else:
            return Dp.newMax((str1[0], str2[0]), Dp.dprec(str1[1:], str2[1:], letters, matrix),
                        ("*", str2[0]), Dp.dprec(str1, str2[1:], letters, matrix),
                        (str1[0], "*"), Dp.dprec(str1[1:], str2, letters, matrix)
                        )


