def binary(a, fir, las, term):
    mid = int((fir+las)/2)
    if term > a[mid]:
        binary(a, mid, las, term)
    elif term < a[mid]:
        binary(a, fir, mid, term)
    elif term == a[mid]:
        print("Number found at", mid+1)
    else:
        print("Number is not there in the array")
    b = [1, 2, 3, 4, 5]
    fir = 0
    las = len(b)
    term = 4
    binary(b, fir, las, term)
