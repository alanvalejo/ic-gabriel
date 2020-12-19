# pip install sumy
# import sumy
# from sumy.summarizers.luhn import LuhnSummarizer

import nltk
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  

sentence = "KARACHI, Pakistan — Iqbal Shaheen, a taxi driver, drove his sick father to this city’s three main hospitals. \
            All of their intensive care beds and ventilators were occupied. \
            Mr. Shaheen was told there might be room at a private hospital, for $625 a day, far above what his earnings \
            of $10 a day could cover. He took his father home to die. \
            The poor cannot afford to be sick,” Mr. Shaheen said. Without political connections, a coronavirus patient \
            cannot get admitted at a public hospital, while paying a private hospital’s bills is unthinkable. \
            As winter sets in, cold weather, pollution and public apathy to the coronavirus are weighing heavily on Pakistan’s limited health care system. \
            Pakistan’s Covid-19 positivity rate has rocketed up to about 7.7 percent of tests administered in recent weeks from only 2 percent in October, \
            prompting a plea from health experts and doctors in Karachi for the government to impose a strict nationwide lockdown."

word_tokens = word_tokenize(sentence)

fd = nltk.FreqDist(word_tokens)
print(fd.keys())
print(fd.most_common())
# fd.plot(cumulative=False)
fd.plot(15, cumulative=False)