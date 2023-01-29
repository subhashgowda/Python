str="What do you think you'll get for your wife?"

words = [word.lower() for word in str.split()]

words.sort()
for word3 in words:
    print(word3)


