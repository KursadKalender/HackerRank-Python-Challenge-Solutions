set_A = set(map(int, input().split()))
number_of_upcoming_sets = int(input())
the_return = True
for i in range(number_of_upcoming_sets):
    upcoming_set = set(map(int, input().split()))
    if not set_A.issuperset(upcoming_set):
       the_return = False
print(the_return) 
