def collatz(n):
    steps = 0
    while(n != 1):
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1 

        steps += 1
    return steps

#print(collatz(2)) #1
#print(collatz(3)) #7
#print(collatz(4)) #2
#print(collatz(5)) #2


res = [0,0]
for i in range(2,1000001):
    
    steps = collatz(i)

    if (steps > res[0]):
        res[0] = steps
        res[1] = i

print(f'Max steps: {res[0]}, Number: {res[1]}')