if __name__ == '__main__':
    num_A = int(input())
    Set_A = set(map(int, input().split()))
    num_others = int(input())
    for i in range(num_others):
        inp_split = input().split()
        other_set = set(map(int, input().split()))
        if inp_split[0] == 'intersection_update':
            Set_A.intersection_update(other_set)
        elif inp_split[0] == 'update':
            Set_A.update(other_set)
        elif inp_split[0] == 'symmetric_difference_update':
            Set_A.symmetric_difference_update(other_set)  
        elif inp_split[0] == 'difference_update':
            Set_A.difference_update(other_set)
    print(sum(Set_A))
