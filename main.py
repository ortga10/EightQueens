BORD_SIZE = 8
zeroBoard = np.zeros(BORD_SIZE * BORD_SIZE, dtype=int).reshape(BORD_SIZE, BORD_SIZE)
ls = np.zeros(BORD_SIZE, dtype=int)
result = []


def isPassing(row, col):
    for i in range(row):
        if ls[i] == col:
            return True
        if ls[i] == col - (row - i):
            return True
        if ls[row - 1 - i] == col + i + 1:
            return True
    return False


def tryToFill(row):
    if row >= len(ls):
        for index, element in enumerate(ls):
            zeroBoard[index][element] = 1
        for x in zeroBoard:
            print(x)
        print(f"columns index = {''.join([str(e) for e in ls])}")
        print("'_*_'" * 5)
        zeroBoard.fill(0)
        result.append(ls)
        return

    for i in range(BORD_SIZE):
        if not isPassing(row, i):
            ls[row] = i
            tryToFill(row + 1)


if __name__ == '__main__':
    tryToFill(0)
    print(f"Total solutions {len( result )}")
