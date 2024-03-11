def order(sentence):
    words = sentence.split(" ")
    orderedWords = []
    for word in words:
        chars=word.split()
        for char in chars:
            if char.isdigit():
                orderedWords[char-1] = word
                continue
    return " ".join(orderedWords)

print(order("is2 Thi1s T4est 3a"))