sentence ="Python is fun"
print("The sentence is:", sentence)

words = sentence.split()
reversed_words = words [::-1]

reversed_sentence = " ".join(reversed_words)
print("The reversed sentence is:" , reversed_sentence)
