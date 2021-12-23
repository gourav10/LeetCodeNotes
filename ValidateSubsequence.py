def isValidSubsequence(array, sequence):
    # Write your code here.
    res = list()
    if(len(array) < len(sequence)):return False
    for i in array:
        if i in sequence:
            res.append(i)
    print(res)
    if(res==sequence):
        return True
    else:
        return False

inp = [1, 1, 1, 1, 1]
seq = [1, 1, 1]
print(isValidSubsequence(inp,seq))
        