
import gensim
from gensim.models import Word2Vec
import nltk

text = "Word2Vec is a technique in Natural Language Processing that converts words into vectors."

tokenized_text = nltk.word_tokenize(text.lower())

sentences = [tokenized_text]

model = Word2Vec(sentences, min_count=1, vector_size=50, window=5, workers=4)

vector = model.wv['word2vec']

print("Vector for 'word2vec':\n", vector)

similar_words = model.wv.most_similar('word2vec', topn=3)
print("\nMost similar words to 'word2vec':", similar_words)

model.save("word2vec_model.model")
