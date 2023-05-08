if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        command = input().strip().split(" ")
        command_itself = command[0]
        if command_itself == 'insert':
            position=int(command[1])
            value=int(command[2])
            arr.insert(position, value)
        elif command_itself=='print':
            print(arr)
        elif command_itself=='remove':
            value_to_remove=int(command[1])
            arr.remove(value_to_remove)
        elif command_itself=='append':
            value_to_append=int(command[1])
            arr.append(value_to_append)
        elif command_itself=='sort':
            arr.sort()
        elif command_itself=='pop':
            arr.pop()
        elif command_itself=='reverse':
            arr.reverse()
