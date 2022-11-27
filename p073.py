d = 12000
count = 0
for i in range(2,d+1):
    start = int(i/3)+1
    end = int(i/2-1e-8) # The very small limit needed to not include 1/2
    for j in range(start, end+1):
        if np.gcd(i,j) == 1:
            count += 1