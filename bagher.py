list_of_strings = []

for _ in range(5):
    data = input("")
    list_of_strings.append(data)

indexes = []
for index, data in enumerate(list_of_strings, start=1):
    if "MOLANA" in data or "HAFEZ" in data:
        indexes.append(index)

if len(indexes) == 0:
    print("NOT FOUND!")
else:
    for index in indexes:
        print(index, end=" ")
