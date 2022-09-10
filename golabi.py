base = input("")

if not(1 <= len(base) <= 20):
    raise Exception("length error")

s = []

for index, value in enumerate(base):
    s.append(base[index:])
    

for value in s:
    while len(value) < len(base):
        value = value[0] + value
    print(value)