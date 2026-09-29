names = ['amit', 'manoj', 'amit']
frequency = {}

for name in names:
    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1
print(frequency)