n = int(input()) #number of elements in the set s.
s = set(map(int, input().split())) #elements of set s.
num_command=int(input())
for i in range(num_command):
    inp = input().split(' ')
    if inp[0] == 'remove':
        s.remove(int(inp[1]))
    elif inp[0] == 'discard':
        s.discard(int(inp[1]))
    else:
        s.pop()
print(sum(s))
