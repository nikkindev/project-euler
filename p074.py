# Using Memoization

fact_digits = lambda number: 0 if number == 0 else math.factorial(number%10)+fact_digits(number//10)

count = 0
global_fact_length = dict()
for n in tqdm(range(1,1000000)):    
    store = {n}
    next_fact = fact_digits(n)
    length = 1
    while next_fact not in store:
        length += 1
        store.add(next_fact)
        if next_fact in global_fact_length:
            length += global_fact_length[next_fact]-1
            break
        else:
            next_fact = fact_digits(next_fact)
            
    global_fact_length[n] = length
    if length == 60:
        count += 1
print(count)