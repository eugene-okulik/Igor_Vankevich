words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
word = list(words.keys())
num = list(words.values())
i = 0

while i < len(words):
    print(word[i] * int(num[i]))
    i += 1
