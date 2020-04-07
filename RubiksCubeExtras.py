def fixSolveString(self):
    b = removeMultiplesOfFour(self.solve)
    c = removeMultiplesOfThree(b)
    self.solve = c

def removeComplement(solve):
    newSolve, j = '', 0
    for i in range(len(solve) - 2):
        a, b = solve[i], solve[i + 1]
        if b == "'":
            if solve[i + 2] == a:
                newSolve += solve[j:i]
                j = i + 3
            elif (i - 1 >= 0) and (solve[i - 1] == a):
                newSolve += solve[j:i - 1]
                j = i + 2
    newSolve += solve[j:len(solve)]
    return newSolve

def removeMultiplesOfFour(solve):
    newSolve, j = '', 0
    i = 0
    while i <= len(solve) - 4:
        a, b, c, d = solve[i], solve[i + 1], solve[i + 2], solve[i + 3]
        if a == b == c == d:
            newSolve += solve[j:i]
            j = i + 4
            i += 4
        else:
            i += 1
    newSolve += solve[j:len(solve)]
    return newSolve

def removeMultiplesOfThree(solve):
    newSolve, j = '', 0
    i = 0
    while i <= len(solve) - 3:
        a, b, c = solve[i], solve[i + 1], solve[i + 2]
        if a == b == c:
            newSolve += solve[j:i + 1]
            newSolve += "'"
            j = i + 3
            i += 3
        else:
            i += 1
    newSolve += solve[j:len(solve)]
    return newSolve
