sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()

eng_uzunlar = []

for word in words:
    eng_uzunlar.append(word)

natija = []

for i in range(3):
    eng_uzun = eng_uzunlar[0]

    for w in eng_uzunlar:
        if len(w) > len(eng_uzun):
            eng_uzun = w

    natija.append(eng_uzun)
    eng_uzunlar.remove(eng_uzun)

print(natija)
