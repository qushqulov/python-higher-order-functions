sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()
words.sort(key=lambda x: len(x), reverse=True)

print(words[:3])
