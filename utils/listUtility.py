def printListOfList(lol, nRow, nCol):
    if nRow == 0:
        nRow = len(lol)
    if nCol == 0:
        nCol = len(lol[0])

    for k in range(nRow):
        print(rooms[k][:nCol])