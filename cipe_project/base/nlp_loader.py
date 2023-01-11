'''
import nltk
from sklearn.feature_extraction.text import CountVectorizer

# Tokenize a sentence
sentence = "This is a sentence that we want to tokenize."
tokens = nltk.word_tokenize(sentence)
print(tokens)

# Create a list of documents
documents = ["This is a document.", "This is another document."]

# Create a CountVectorizer object
vectorizer = CountVectorizer()

# Tokenize and vectorize the documents
vectors = vectorizer.fit_transform(documents)

# Print the vocabulary
print(vectorizer.vocabulary_)

# Print the resulting vectors
print(vectors.toarray())

'''


'''
['This', 'is', 'a', 'sentence', 'that', 'we', 'want', 'to', 'tokenize', '.']
{'this': 4, 'is': 1, 'document': 0, 'another': 2}
[[1 1 0 0 1 0 0 0 0]
 [1 1 0 0 1 0 0 0 0]]
'''