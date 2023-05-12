if __name__ == '__main__':
    happiness = 0
    N,M = map(int, input().split())
    the_array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    for i in the_array:
        if i in A:
            happiness = happiness + 1
        elif i in B:
            happiness = happiness - 1
        else:
            happiness = happiness
    
    print(happiness)
