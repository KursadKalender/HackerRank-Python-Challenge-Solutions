if __name__ == '__main__':
    full_list=[]
    names=[]
    scores=[]
    end=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        full_list.append([name, score])
        names.append(name)
        scores.append(score)
    second_worst=sorted(set(scores), reverse=True)[-2]
    
    for i in range(len(full_list)):
        if full_list[i][1] == second_worst:
            end.append(full_list[i][0])

    print('\n'.join(sorted(end)))
    
