# -*- coding: utf-8 -*-
"""
    @author: can-j

    Google Play Store'daki Uygulamaların  Kategori Analizi
         WordCloud Visualization
"""

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('googleplaystore.csv')

sorted_dataset = dataset.sort_values(by=['Category']) # veriler sıralandırıldı
categories = sorted_dataset['Category'][1:] # gereksiz veriler temizlendi

comment_words = ' '

for val in categories: 
    val = str(val) 
    tokens = val.split() 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    for words in tokens: 
        comment_words = comment_words + words + ' ' 
    #kategoriler tek string halinde comment_words'e eklendi

#print(comment_words) # bütün uygulamaların kategorileri yazdırıldı

from wordcloud import WordCloud, STOPWORDS
wordcloud = WordCloud(background_color='white', stopwords=STOPWORDS,
                      max_words=200, max_font_size=70,collocations=False,
                      random_state=30).generate(comment_words)

fig = plt.figure(figsize = (5, 5), facecolor = None) 
# resimi düzeltmek için uygulanan filtre (gaussian,bilinear..)
plt.imshow(wordcloud, interpolation = 'bilinear') 
plt.axis('off')                             
plt.show()
#fig.savefig("pltword.png", dpi=900) # resim formatında kaydetme