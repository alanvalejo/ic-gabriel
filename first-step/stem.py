# https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
# O stemming é uma espécie de normalização das palavras.
# Normalização é uma técnica em que um conjunto de palavras em uma frase é convertido em uma 
# sequência para encurtar sua pesquisa. As palavras que têm o mesmo significado, mas apresentam 
# alguma variação de acordo com o contexto ou frase, são normalizadas.
# Em outra palavra, existe uma palavra raiz, mas existem muitas variações das mesmas palavras. 
# Por exemplo, a palavra raiz é "comer" e suas variações são "comer, comer, comer e assim por diante". 
# Da mesma forma, com a ajuda de Stemming, podemos encontrar a palavra raiz de qualquer variação.

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

sentence = "Hello Guru99, You have to build a very good site and I love visiting your site."

words = word_tokenize(sentence)
porter = PorterStemmer()
lancaster = LancasterStemmer()

for word in words:
    print("{0:20}{1:20}{2:20}".format(word, porter.stem(word), lancaster.stem(word)))