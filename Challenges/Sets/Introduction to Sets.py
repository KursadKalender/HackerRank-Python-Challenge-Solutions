def average(array):
    array_set= set(array)
    total_number=len(array_set)
    return "{:.3f}".format(sum(array_set)/total_number) 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
