# -*- coding: utf-8 -*-
"""감성분석.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D_qG_y2gCe9rD9OkyZhakkN2-2-peW28
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import torch

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
device

# Commented out IPython magic to ensure Python compatibility.
# # 샘플 데이터로는 github에 올려져 있는 네이버 영화 감상평에 대한 감성 분석 예제를 이용한다
# 
# %%time
# !rm -f ratings_train.txt ratings_test.txt
# !wget -nc https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt
# !wget -nc https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt

# 여기에서는 유니코드로 인코딩하며 읽기 위해 codecs 패키지를 사용한다. 
# 읽어들인 결과는 유니코드 문자열이 된다.
import codecs

with codecs.open("ratings_train.txt",encoding="utf-8") as f:
    data=[line.split('\t') for line in f.read().splitlines()]
    data=data[1:] # header 제외

data
# 데이터는 [[번호,내용, 평점,긍/부정],[..]]으로 이뤄짐.

# 내용을 X로, 평점을 Y로 저장
from pprint import pprint
pprint(data[0])

X=list(zip(*data))[1]
Y=np.array(list(zip(*data))[2],dtype=int)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

model1=Pipeline([
                 ('vect',CountVectorizer()),
                 ('mb',MultinomialNB())
])
model1.fit(X,Y)

with codecs.open("ratings_test.txt",encoding='utf-8') as f:
    data_test=[line.split("\t") for line in f.read().splitlines()]
    data_test=data_test[1:] # header 제외
data_test

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import torch

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
device

# Commented out IPython magic to ensure Python compatibility.
'''
앞에서 공부한 나이브 베이즈 분류 모형을 이용하여 문서에 대한 감성 분석(sentiment analysis)를 해보자. 
감성 분석이란 문서에 대해 좋다(positive) 혹은 나쁘다(negative)는 평가를 내리는 것을 말한다.
샘플 데이터로는 github에 올려져 있는 네이버 영화 감상평에 대한 감성 분석 예제를 이용한다.
'''
# %time
!rm -f ratings_train.txt ratings_test.txt
!wget -nc https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt
!wget -nc https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt

# 여기에서는 유니코드로 인코딩하며 읽기 위해 codecs 패키지를 사용한다. 
# 읽어들인 결과는 유니코드 문자열이 된다.

import codecs
with codecs.open("ratings_train.txt",encoding="utf-8") as f:
    data=[line.split("\t") for line in f.read().splitlines()]
    data=data[1:] #header 제외
data

# 이 데이터는 번호, 내용, 평점으로 이루져 있으므로 내용을 X, 평점을 y로 저장한다.
X=list(zip(*data))[1]
Y=np.array(list(zip(*data))[2],dtype=int)

# 이 데이터를 다항 나이브 베이즈 모형으로 학습시킨다.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

model1=Pipeline([
                 ('vect',CountVectorizer()),
                 ('mb',MultinomialNB()),
])

result1=model1.fit(X,Y)

# 테스트 데이터로 모형 성능 측정
import codecs
with codecs.open("ratings_test.txt",encoding="utf-8") as f:
    data_test=[line.split("\t") for line in f.read().splitlines()]
    data_test=data_test[1:] #header 제외
data_test

X_test=list(zip(*data_test))[1]
Y_test=np.array(list(zip(*data_test))[2],dtype=int)
Y_pred=result1.predict(X_test)

print(classification_report(Y_test,Y_pred))

# Tfidf로 모델과 비교
from sklearn.feature_extraction.text import TfidfVectorizer

model2=Pipeline([
                 ('vect',TfidfVectorizer()),
                 ('mb',MultinomialNB()),
])
result2=model2.fit(X,Y)
Y_pred2=result2.predict(X_test)
print(classification_report(Y_test,Y_pred2))

# 형태소 분석기를 사용한 결과와 비교
!pip install konlpy

from konlpy.tag import Okt
pos_tagger = Okt()

# 형태소 분석기
def tokenize_pos(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc)]

model3=Pipeline([
                 ('vect',CountVectorizer(tokenizer=tokenize_pos)),
                 ('mb',MultinomialNB()),
])

result3=model3.fit(X,Y)
Y_pred3=result3.predict(X_test)
print(classification_report(Y_test,Y_pred3))

# ngram NLP모델
model4 = Pipeline([
    ('vect', TfidfVectorizer(tokenizer=tokenize_pos, ngram_range=(1, 2))),
    ('mb', MultinomialNB()),
])
result4=model4.fit(X,Y)
Y_pred4=result4.predict(X_test)
print(classification_report(Y_test,Y_pred4))

