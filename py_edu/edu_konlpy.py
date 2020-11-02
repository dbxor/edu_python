#%%
from konlpy.tag import Kkma #한국어 정보처리
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud #시각화

from collections import Counter
import numpy as np 

#"문장 -> 단어 -> 키원드 -> 필터링 -> 집계 -> 시각화"
kkma = Kkma()

data1 = open("yeosu.txt").read()

data2 = kkma.nouns(data1)
data3 = Counter(data2)

stop_words = open("").read()

data3 = [each_word for each_word in data2
            if each_word not in stop_words]

data4 = []
for i in range(0, len(data3)) :
    if len(data3[i]) >=2 | len(data3[i]) <= 10 :
        data4.append(data3[i])

data5 = Counter(data4)
data6 = data5.most_common(100)
tmp_data = dict(data6)

