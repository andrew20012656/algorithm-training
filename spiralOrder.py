def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    xstart, ystart = 0, 0
    row, col = len(matrix), len(matrix[0])
    offset = min(row // 2, col // 2)
    result = []
    
    for i in range(1,offset + 1):
        for i in range(ystart, col - offset):
            result.append(matrix[xstart][i])
        for i in range(xstart, row - offset):
            result.append(matrix[i][col-offset])
        for i in range(col - offset, ystart, -1):
            result.append(matrix[row-offset][i])
        for i in range(row - offset, xstart, -1):
            result.append(matrix[i][ystart])
        xstart += 1
        ystart += 1
    if row % 2 != 0:
        index = row // 2
        for i in range(offset, col - offset):
            result.append(matrix[index][i])
    elif col % 2 != 0:
        index = col //2
        for i in range(offset, col - offset):
            result.append(matrix[i][index])
    return result

print(spiralOrder([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]))