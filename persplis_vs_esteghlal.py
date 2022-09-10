result = []


rep = int(input(""))

if not (1 <= rep <= 1000):
    raise Exception("Invalid input")

for _ in range(rep):
    scores = input("")
    scores = scores.split(" ")
    
    for check in scores:
        if not(0 <= int(check) <= 6):
            raise ValueError("More than 6 or less 0")

    perspolis: list = []
    perspolis.append(scores[0])
    perspolis.append(scores[2])
    esteghlal: list = []
    esteghlal.append(scores[1])
    esteghlal.append(scores[3])

    sum_pers = sum([int(x) for x in perspolis])
    sum_esth = sum([int(x) for x in esteghlal])

    if sum_pers > sum_esth:
        result.append("perspolis")
    elif sum_esth > sum_pers:
        result.append("esteghlal")
    else:
        if int("".join(perspolis)) > int("".join(esteghlal)):
            result.append("perspolis")
        elif int("".join(esteghlal)) == int("".join(perspolis[::-1])) :
            result.append("penalty")
        elif int("".join(esteghlal)) > int("".join(perspolis)):
            result.append("esteghlal")

for res in result:
    print(res)
    