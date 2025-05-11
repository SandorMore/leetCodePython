n = int(input())

s = set(map(int, input().split()))

num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    operation = command[0]
    
    if operation == "pop":
        if s:  
            s.pop()
    elif operation == "remove":

        value = int(command[1])
        if value in s:
            s.remove(value)
    elif operation == "discard":

        value = int(command[1])
        s.discard(value)

print(sum(s))