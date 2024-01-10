prime = []

for i in range(1, 5):
    if i * i > 4:
        break
    if 4 % i == 0:
        prime.append(i)
        prime.append(4 // i)
print(prime)