if __name__ == '__main__':
    eng_sub = int(input())
    eng_numbers = set(map(int, input().split()))
    fr_sub = int(input())
    fr_numbers = set(map(int, input().split()))
    print(len(eng_numbers.difference(fr_numbers)))
