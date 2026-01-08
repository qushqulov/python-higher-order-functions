data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

natija = []

for x in data:
    if type(x) == str:      
        if len(x) > 5:       
            natija.append(x)

print(natija)
