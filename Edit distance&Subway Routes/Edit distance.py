import numpy as np

def editDistance(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    
    n = len(list1)
    m = len(list2)
    
    A = np.zeros((n+1, m+1))

    for i in range(n+1):
        A[i][0] = i
        
    for j in range(m+1):
        A[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if list1[i-1] == list2[j-1]:
                A[i][j] = A[i-1][j-1]
            else:
                A[i][j] = min(A[i-1][j], A[i][j-1], A[i-1][j-1]) + 1
                
    return int(A[n][m])

if __name__ == "__main__":
    str1 = "cat"
    str2 = "dog"
    str3 = "category"

    result = editDistance(str1, str2)
    result2 = editDistance(str1, str3)
    print(f"'{str1}'와(과) '{str2}' 사이의 편집 거리는 {result}입니다.")
    print(f"'{str1}'와(과) '{str3}' 사이의 편집 거리는 {result2}입니다.")






