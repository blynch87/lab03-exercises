def find_duplicates_nested_loop(l: list) -> list:
    newList = []
    listSize = len(l)

    for x in range(0, listSize -1):
        for y in range(x+1, listSize):
            if l[x] == l [y]:
                if l[x] not in newList:
                    newList.append(l[x])  # or index = 0
                                          # newlist[index] = l[x]
                                          # index += 1
    
    return newList

if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates_nested_loop(sample1))
    print("Sample 2:", find_duplicates_nested_loop(sample2))
    print("Sample 3:", find_duplicates_nested_loop(sample3))
    print("Sample 4:", find_duplicates_nested_loop(sample4))
