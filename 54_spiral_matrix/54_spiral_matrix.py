class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []  # Create an empty list to store the result

        while matrix:  # Continue until the matrix is empty
            # Step 1: Move from left to right and append the first row to the result
            result += matrix.pop(0)

            # Step 2: Move from top to bottom and append the last column to the result
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # Step 3: Move from right to left and append the last row (reversed) to the result
            if matrix:
                result += matrix.pop()[::-1]

            # Step 4: Move from bottom to top and append the first column to the result
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result