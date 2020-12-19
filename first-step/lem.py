import nltk
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

lancaster = LancasterStemmer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)

for w in tokenization:
    print("Stemming for {} is {}".format(w, lancaster.stem(w)))

wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w))) 