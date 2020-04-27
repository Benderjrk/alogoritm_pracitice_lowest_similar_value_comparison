def lowest_similar_value_comparison(A, B):
    A.sort()
    B.sort()
    i = 0
    # loop though the A array
    for a in A:
        
        while i < len(B) and B[i] < a:
            i += 1
            if a == B[i]:
                return a
    return -1
