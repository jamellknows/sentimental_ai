import sentimental_analyser



sentence1 = "I"
sentence2 = "a"
sentence3 = sentence1 + " " + sentence2
res1 = sentimental_analyser.sentiment(sentence1)
res2 = sentimental_analyser.sentiment(sentence2)
res3 = sentimental_analyser.sentiment(sentence3)
print(f" Sentence 1 results are {res1} \n Sentence 2 results are {res2} \n Sentence 3 results are {res3} \n")

sentence1 = "I'm happy"
sentence2 = "I'm full of happiness"
sentence3 = sentence1 + " " + sentence2
res1 = sentimental_analyser.sentiment(sentence1)
res2 = sentimental_analyser.sentiment(sentence2)
res3 = sentimental_analyser.sentiment(sentence3)
print(f" Sentence 1 results are {res1} \n Sentence 2 results are {res2} \n Sentence 3 results are {res3} \n")