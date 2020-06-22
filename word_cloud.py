import pandas as  pd 
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
def word_cloud(document):
    #instantiate a wordcloud object
    stopwords = set(STOPWORDS)
    stopwords.add('said')
    alice_wc = WordCloud(
        background_color="white",
        max_words=2000,
        stopwords=stopwords
    )
    alice_wc.generate(alice_data)
    plt.imshow(alice_wc,interpolation = 'bilinear')
    plt.axis('off')
    plt.show()
if __name__ == '__main__':
    
    path = r"D:\IBM Certification\dataVisualization\alice_novel.txt"

    alice_data = open(path,'r').read()
    word_cloud(alice_data)
