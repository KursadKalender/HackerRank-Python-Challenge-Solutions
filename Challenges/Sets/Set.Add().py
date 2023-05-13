if __name__ == '__main__':
    number = int(input())
    my_set=set()
    for i in range(number):
       item=input()
       my_set.add(item)
    
    print(len(my_set))
