def _transfer(L):
    string = ''.join([str(i) for i in L])
    num = int(string, base=2)
    return num

def is_contained(A, B):
    bA = _transfer(A)
    bB = _transfer(B)
    res = bA | bB
    if res == bB:
        return True
    else:
        return False

