if __name__ == '__main__':
    M = int(input())
    Set_M = set(map(int, input().split()))
    N = int(input())
    Set_N = set(map(int, input().split()))
    MN = Set_M.difference(Set_N)
    NM = Set_N.difference(Set_M)
    UNI = MN.union(NM)
    for i in sorted(UNI):
        print(i)
