import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url="https://www.ndtv.com/india-news/no-local-poll-without-obc-quota-yogi-adityanath-after-setback-in-court-3641956"
article=Article(url)
article.download()
article.parse()
article.nlp()
print(f'Title :{article.title}')
print(f'Author :{article.authors}')
print(f'Publication Date :{article.publish_date}')
print(f'Summary :{article.summary}')

