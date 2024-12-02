# NLP
# pos tagging
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "stemming helps in preprocessing text"
words = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print(pos_tags)
