if __name__ =='__main__':
    n = int(input()) #number of students who subscribed to english paper.
    eng_set = set(map(int, input().split(' ')))
    b = int(input()) #number of students who subscribed to french paper.
    fr_set = set(map(int, input().split(' ')))
    
    print(len(eng_set.union(fr_set)))
