class Dp:

    @staticmethod
    def value(i, j, dic, letters):
        return int(dic[(i,j)])

    @staticmethod
    def valueAll(tp, dic, letters):
        sum = 0
        for i in range(len(tp[0])): 
            key = tp[0][i]  
            value = tp[1][i] 
            if key == '*' or value == '*':
                sum = sum - 4
            else:
                sum = sum + Dp.value(key, value, dic, letters)
        return sum


    @staticmethod
    def newMax(tp1, tp2, tp3, dic, letters):
        value1 = Dp.valueAll(tp1, dic, letters)
        value2 = Dp.valueAll(tp2, dic, letters)
        value3 = Dp.valueAll(tp3, dic, letters)
        best = max(value1, value2, value3)
        if best == value1:
            return tp1
        elif best == value2:
            return tp2
        else:
            return tp3

    @staticmethod
    def dprec(str1, str2, letters, dic, memo):
        if (str1, str2) in memo: 
            return memo[(str1, str2)]
        if len(str1) == 0 and len(str2) == 0:
            return ("","")
        elif len(str1) == 0:
            return ('*' * len(str2), str2)
        elif len(str2) == 0:
            return (str1, '*' * len(str1))
        else:
            keep = Dp.dprec(str1[1:], str2[1:], letters, dic, memo)
            switchL = Dp.dprec(str1, str2[1:], letters, dic, memo)
            switchR = Dp.dprec(str1[1:], str2, letters, dic, memo)
            result = Dp.newMax(
                        (str1[0] + keep[0], str2[0] + keep[1]),
                        ('*' + switchL[0], str2[0] + switchL[1]), 
                        (str1[0] + switchR[0], '*' + switchR[1]),
                        dic, 
                        letters
                        )
            memo[(str1, str2)] = result 
            return result


