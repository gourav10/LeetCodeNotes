def isValidSequence(array,sequence):
    for num in sequence:
        if(num not in array):
            return False
    return True

if __name__=="__main__":
    arr = [5,1,22,25,6,-1,8,10]
    seq = [1,6,-1,-1,10]