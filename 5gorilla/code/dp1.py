class Dp1:

    @staticmethod
    def value(i, j, matrix, letters):
        """Retrieve the cost of aligning two characters from the matrix."""
        return int(matrix[letters.index(i)][letters.index(j)])

    @staticmethod
    def dp(str1, str2, letters, matrix, memo):
        """Recursive dynamic programming function with memoization to find the minimum alignment cost."""
        if (str1, str2) in memo:
            return memo[(str1, str2)]

        if len(str1) == 0:
            return -4 * len(str2)  # Cost of aligning remaining str2 with gaps
        if len(str2) == 0:
            return -4 * len(str1)  # Cost of aligning remaining str1 with gaps

        # Recursive cases
        cost_match = Dp1.value(str1[0], str2[0], matrix, letters) + Dp1.dp(str1[1:], str2[1:], letters, matrix, memo)
        cost_insert = -4 + Dp1.dp(str1, str2[1:], letters, matrix, memo)  # Insert gap in str1
        cost_delete = -4 + Dp1.dp(str1[1:], str2, letters, matrix, memo)  # Insert gap in str2

        min_cost = max(cost_match, cost_insert, cost_delete)
        memo[(str1, str2)] = min_cost
        return min_cost

    @staticmethod
    def align(str1, str2, letters, matrix):
        """Compute the alignment using dynamic programming and memoization."""
        memo = {}
        Dp1.dp(str1, str2, letters, matrix, memo)
        
        # Building the aligned sequences
        aligned1, aligned2 = "", ""
        while str1 and str2:
            if (str1, str2) in memo and memo[(str1, str2)] == Dp1.value(str1[0], str2[0], matrix, letters) + memo.get((str1[1:], str2[1:]), 0):
                aligned1 += str1[0]
                aligned2 += str2[0]
                str1, str2 = str1[1:], str2[1:]
            elif (str1, str2) in memo and memo[(str1, str2)] == -4 + memo.get((str1, str2[1:]), 0):
                aligned1 += '*'
                aligned2 += str2[0]
                str2 = str2[1:]
            else:
                aligned1 += str1[0]
                aligned2 += '*'
                str1 = str1[1:]

        # If there are remaining characters in either string
        aligned1 += str1 or '*' * len(str2)
        aligned2 += str2 or '*' * len(str1)

        return aligned1, aligned2