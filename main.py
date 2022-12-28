import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = "https://www.ndtv.com/india-news/no-local-poll-without-obc-quota-yogi-adityanath-after-setback-in-court-3641956"
article = Article(url)
article.download()
article.parse()
article.nlp()
print(f'Title :{article.title}')
print(f'Author :{article.authors}')
print(f'Publication Date :{article.publish_date}')
print(f'Summary :{article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(
    f'Sentiments :{"Positive" if analysis.polarity >0 else "Negative" if analysis.polarity<0 else "Netural"}')

# Bulding GUI
root = tk.Tk()
root.title = ("Article Summarizer")
root.geometry = ('1200x600')
# Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disable', bg='#D3D3D3')
title.pack()
# author
alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disable', bg='#D3D3D3')
author.pack()
# Publication date
plabel = tk.Label(root, text='Publication Date')
plabel.pack()
publicatin_date = tk.Text(root, height=1, width=140)
publicatin_date.config(state='disable', bg='#D3D3D3')
publicatin_date.pack()
# summary
slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disable', bg='#D3D3D3')
summary.pack()
# Sentiments
selabel = tk.Label(root, text='Sentiments Analysis')
selabel.pack()
sentiments = tk.Text(root, height=1, width=140)
sentiments.config(state='disable', bg='#D3D3D3')
sentiments.pack()
# url
ulabel = tk.Label(root, text='URL')
ulabel.pack()
url = tk.Text(root, height=1, width=140)
url.pack()
# Button
btn = tk.Button(root, text='Submit',)
btn.pack()
root.mainloop()
