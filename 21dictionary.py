d = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
}
a = d.values()
a = [int(num) for num in a]
for num in a:
    if num < 2:
        print(num,":not prime pair ")
        continue
    prime = True
    for i in range(2, int(num**.5) +1 ):
        if num % i == 0:
            prime= False
            break
    if prime:    
        print(num,":prime pair ")
    else:
        print(num,":not prime pair ")
