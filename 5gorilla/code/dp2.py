import numpy 

class Dp2:
    
    @staticmethod
    def computeF(A, B, S):
        #A, B = compare
        d = -4
        F = numpy.zeros((len(A)+1, len(B)+1), dtype=int) 

        for i in range(len(A)+1):
            F[i,0] = d * i
        for j in range(len(B)+1):
            F[0,j] = d * j

        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                matches = int(F[i-1, j-1]) + int(S[(A[i-1],B[j-1])]) #int(S[A[i-1]][B[j-1]])
                delete = F[i-1, j] + d
                insert = F[i, j-1] + d
                F[i,j] = max(matches, insert, delete)

        return F

    @staticmethod
    def alignment(A, B, F, S):
        alignmentA = ""
        alignmentB = ""
        d = -4
        #word1, word2 = comp
        i = len(A)
        j = len(B)
        #print(A)
        #print(B)
        #print("")

        while (i > 0) or (j > 0):
            if i > 0 and j > 0 and int(F[i, j]) == (int(F[i-1, j-1]) + int(S[(A[i-1],B[j-1])])): #int(S[[i-1]][word2[j-1]])):
                alignmentA = A[i-1] + alignmentA
                alignmentB = B[j-1] + alignmentB
                i -= 1
                j -= 1
            elif (i > 0 and F[i, j] == F[i-1, j] + d):
                alignmentA = A[i-1] + alignmentA
                alignmentB = "*" + alignmentB
                i -= 1
            else:
                alignmentA = "*" + alignmentA
                alignmentB = B[j-1] + alignmentB
                j -= 1

        return alignmentA + " " + alignmentB
