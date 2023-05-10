if __name__ == '__main__':
    inputs = input().split()
    N = int(inputs[0])
    M = int(inputs[1])
    s = 1

    for line in range(N+1):
        if line < int(N/2):
            print((".|."*s).center(M, "-"))
            s += 2
        elif line == round(N/2):
            print("WELCOME".center(M, "-"))
        elif line > int(N/2) and s > 1:
            s -= 2
            print((".|."*s).center(M, "-"))
