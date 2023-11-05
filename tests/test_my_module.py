import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from wordcloud import WordCloud 

import nltk.corpus
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Flipkart Product Reviews - Kaggle/Dataset-SA.csv')
data['sentiment_code'] = pd.Categorical(data.Sentiment).codes
data['sentiment_code'] = data['sentiment_code'].astype('Int64')
data.dropna(inplace = True)
