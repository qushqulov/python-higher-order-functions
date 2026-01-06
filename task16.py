data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

print(list(filter(lambda x: isinstance(x, str) and len(x) > 5, data)))
