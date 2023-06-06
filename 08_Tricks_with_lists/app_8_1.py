text = "The Zen of Python"
list = text.split()
result = " ".join(map(lambda x: x + "!", list))
print(result)
