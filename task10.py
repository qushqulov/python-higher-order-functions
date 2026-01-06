text = ["apple", "34", "banana", "100", "abc", "75"]

raqamlar = []
for x in text:
    if x.isdigit():
        raqamlar.append(x)

print(raqamlar)
